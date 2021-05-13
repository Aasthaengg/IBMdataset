import sys
input = sys.stdin.readline

n, s, ind, res = int(input()), list(map(int, input().split())), 1, 0
for i in s:
    if i == ind: ind += 1
    else: res += 1
print(-1 if res == n else res)