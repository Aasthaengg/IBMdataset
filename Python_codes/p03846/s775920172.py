N = int(input())
a = list(map(int,(input().split())))
MOD = 10**9 + 7
a.sort()

ans = []
if N%2 == 0:
    for i in range(N):
        ans.append(2*(i//2)+1)
    if ans == a:
        print(pow(2,N//2,MOD))
    else:
        print(0)
else:
    for i in range(N):
        ans.append(2*((i+1)//2))
    if ans == a:
        print(pow(2,(N-1)//2,MOD))
    else:
        print(0)