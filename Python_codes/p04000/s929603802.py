from collections import defaultdict
import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
ans = [0] * 10
ans[0] = (H - 2) * (W - 2)
# print (ans)
tmplst = [-1, 0, 1]
dic = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in tmplst:
        if 0 <= a + i <= H - 1:
            for j in tmplst:
                if 0 <= b + j <= W - 1: #範囲に入っている
                    tmp = dic[(a + i, b + j)]
                    dic[(a + i, b + j)] += 1
                    if 1 <= a + i <= H - 2 and 1 <= b + j <= W - 2:
                        ans[tmp] -= 1
                        ans[tmp + 1] += 1

print (*ans, sep = '\n')