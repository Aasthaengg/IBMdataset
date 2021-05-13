import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


n = ni()
res = [list(input().split() + [i + 1]) for i in range(n)]
res = list(map(lambda x: (x[0], int(x[1]), x[2]), res))
res = sorted(res, key=lambda x: x[0])
start = 0
start_res = res[0][0]
sor_res = []
ans = []
for i in range(n):
    if start_res != res[i][0]:
        end = i - 1
        sor_res += sorted(res[start:end + 1], key=lambda x: x[1], reverse=True)
        start = i
        start_res = res[i][0]
    if i == n - 1:
        end = i
        sor_res += sorted(res[start:end + 1], key=lambda x: x[1], reverse=True)
for r in sor_res:
    print(r[2])
