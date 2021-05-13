# 2020/07/15
# AtCoder Grand Contest 006 - A

# Input
n = int(input())
s = input()
t = input()
ans = n * 2

for i in range(n):
    j = 0
    while i + j < n :
        if s[i+j] != t[j]:
            break
        j = j + 1

    if i + j == n:
        ans = j + i * 2
        break

print(ans)