n = int(input())
s = list(map(int, input().split()))
a = 0
for j in range(n):
    if (j + 1) * int(s[j]) % 2 != 0:
        a += 1

print(a)