N = int(input())
L = list(map(int, input().split()))
x = sorted(L)
Lmax = max(L)
y = x[0:-1]
ysum = sum(y)
print("Yes" if Lmax < ysum else "No")
