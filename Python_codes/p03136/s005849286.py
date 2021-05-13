N = int(input())
L = list(map(int,input().split()))
lmax = max(L)
ltot = sum(L)
if ltot>2*lmax:
    print("Yes")
else:
    print("No")