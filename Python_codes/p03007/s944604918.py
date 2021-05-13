N=int(input())
A=list(map(int,input().split()))
B=list(map(lambda x:abs(x),A))

A.sort()
for i in range(N):
    if A[i]>0:
        break
hu=A[:i]
sei=A[i:]

l=[]
if sei and hu:
    ans=sei.pop(-1)
    for item in sei:
        l.append([hu[0],item])
        hu[0]-=item
    for item in hu:
        l.append([ans,item])
        ans-=item

elif sei:
    ans=sei.pop(-1)
    for i in range(len(sei)-1):
        l.append([sei[0],sei[i+1]])
        sei[0]-=sei[i+1]
    l.append([ans,sei[0]])
    ans-=sei[0]
elif hu:
    for i in range(len(hu)-1):
        l.append([hu[-1],hu[-i-2]])
        hu[-1]-=hu[-i-2]
    ans=hu[-1]

print(ans)
for item in l:
    print(*item)