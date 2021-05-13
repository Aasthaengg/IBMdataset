N = int(input())
L = list(map(int,input().split()))

Lmax = max(L)
Lsum = sum(L) - Lmax

if Lmax < Lsum:
    ans = "Yes"
else:
    ans = "No"

print(ans)