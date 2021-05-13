from sys import stdin
def input():
    return stdin.readline().strip()

n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

s.sort()

ans = sum(s)

if ans % 10 != 0:
    print(ans)
    exit()

for i in s:
    if i % 10 != 0:
        print(ans - i)
        exit()
else:
    print(0)