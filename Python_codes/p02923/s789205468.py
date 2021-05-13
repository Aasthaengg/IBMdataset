N=int(input())
H=list(map(int,input().split()))
count=0
ans=[]

for i in range(1,len(H)):
    if H[-i]<=H[-i-1]:
        count+=1
    else:
        ans.append(count)
        count=0
ans.append(count)
print(max(ans))