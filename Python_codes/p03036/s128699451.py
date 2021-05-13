import sys
input = lambda : sys.stdin.readline().rstrip()

r, d, x_2000 = map(int, input().split())

ans = [x_2000]

for i in range(10):
    ans.append(r*ans[-1] - d)

for i in range(1, 11):
    print(ans[i])
