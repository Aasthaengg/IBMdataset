n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n - 1):
    if s[i] == "R" and s[i + 1] == "L":
        cnt += 2
if s[0] == "L":
    cnt += 1

if s[-1] == "R":
    cnt += 1

happy = n - cnt

print(min(happy + k * 2, n - 1))
