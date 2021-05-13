n, x = (int(i) for i in input().split())
M = [None] * n
for i in range(n):
    M[i] = int(input())

ans = n
last = x - sum(M)
add_make = last // min(M)
print(ans + add_make)
