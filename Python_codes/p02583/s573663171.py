import math

n = int(input())
s = list(map(int, input().split()))
s.sort()

cnt = 0
for i in range(n-2):
    for j in range(i, n-1):
        for k in range(j, n):
            if s[i] == s[j] or s[j] == s[k]:
                pass
            else:
                if s[i] + s[j] > s[k]:
                    cnt += 1

print(cnt)

