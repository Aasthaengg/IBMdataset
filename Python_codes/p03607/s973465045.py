N = int(input())
al = [int(input()) for _ in range(N)]

num_dic = {}
for a in al:
    num = num_dic.get(a, 0)
    num_dic[a] = 1 if num == 0 else 0

ans = 0
for k, v in num_dic.items():
    if v != 0:
        ans += 1

print(ans)
