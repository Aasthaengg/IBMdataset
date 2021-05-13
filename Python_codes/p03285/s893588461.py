N=int(input())
res=False
for i in range(N//7+1):
    if (N-7*i)%4==0:
        res=True
        break

if res:
    print("Yes")
else:
    print("No")
