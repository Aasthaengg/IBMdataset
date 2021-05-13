import sys
input = sys.stdin.readline

N, = map(int, input().split())
L = [int(v) for v in input().split()]
c = max(L) + 1

ans = 0
for i in range(N - 1):
    if L[i] == L[i + 1]:
        L[i + 1] = c
        c += 1
        ans += 1
        
print(ans)