import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
ans = []

for i in range(n):
    temp = 0
    for j in range(len(b)):
        if j+1 == b[j]:
            temp = max(temp, b[j])
    if temp == 0:
        ans = [-1]
        break
    ans.insert(0, temp)
    b.pop(temp-1)

print('\n'.join(map(str, ans)))
