n = int(input())
a = list(map(int, input().split()))
chk = 0
for i in range(n):
    chk ^= a[i]
print("Yes" if chk == 0 else "No" )