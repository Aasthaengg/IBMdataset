import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
ans = []
for i in range(1, n + 1):
    cnt += i
    ans.append(i)
    if cnt >= n:
        if cnt > n:
            ans.remove(cnt - n)
        for j in range(len(ans)):
            print(ans[j])
        exit()
