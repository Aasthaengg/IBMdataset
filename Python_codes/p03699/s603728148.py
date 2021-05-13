import sys
input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]

s_ls = sorted([w for w in ls if w % 10 != 0])
ans = sum(s_ls)

if ans == 0:
    print(0)
    exit()

if ans % 10 == 0:
    ans -= s_ls[0]

ans += sum([w for w in ls if w % 10 == 0])
print(ans)
