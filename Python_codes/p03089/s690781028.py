import sys

n = int(input())
b = list(map(int, input().split()))
ans = []
for i in range(n):
    for j in range(len(b), 0, -1):
        if b[j - 1] == j:
            ans.append(j)
            del b[j - 1]
            break
    else:
        print(-1)
        sys.exit()
ans.reverse()
for i in ans:
    print(i)