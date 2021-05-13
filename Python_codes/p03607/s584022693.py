from sys import stdin
def input():
    return stdin.readline().strip()

n = int(input())

a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

i = 0
ans = 0
while i < n:
    num = 1
    i += 1
    while i < n and a[i] == a[i-1]:
        num += 1
        i += 1
    if num % 2 == 1:
        ans += 1

print(ans)