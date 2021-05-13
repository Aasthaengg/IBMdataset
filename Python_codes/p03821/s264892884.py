n = int(input())
ab_list = []
for i in range(n):
    a, b = map(int, input().split())
    ab_list.append([a, b])
cnt = 0
for a, b in ab_list[::-1]:
    tmp_cnt = b - ((cnt + a) % b if (cnt + a) % b != 0 else b)
    cnt += tmp_cnt
print(cnt)