import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
ans = set()
for i in range(n):
    j = a[i] - 1
    if (i not in ans) and (j not in ans) and a[j] == i + 1:
        ans.add(j)
print(len(ans))
