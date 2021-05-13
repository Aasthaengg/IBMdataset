N=int(input())
H=list(map(int,input().split()))
x=0
l=[]
for i in range(N-1):
    if H[i]>=H[i+1]:
        x+=1
    else:
        l.append(x)
        x=0
l.append(x)
print(max(l))