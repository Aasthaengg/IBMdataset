N=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

can = sum(b)-sum(a)
actA,actB = 0,0
for i in range(N):
    diff = b[i]-a[i]
    if diff==0:continue
    if diff>0:
        actA+=(diff+1)//2
        actB+=diff%2
    else:
        actB+=(-diff)
leftA = can-actA
leftB = can-actB
print("Yes" if leftA>=0 and leftA*2==leftB else "No")
