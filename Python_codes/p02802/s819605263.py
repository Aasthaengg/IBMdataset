
n, m = (int(x) for x in input().split())

# 0 = まだACなし, 1 = AC済み
ans_list = [0] * (n + 1)
# 誤った回数が記録され、ACのタイミングで加算
WA_list = [0] * (n + 1)

ans = 0
penalty = 0

for id in range(m):
    # listを紐付けて要素を抜き出すことができる
    query = list(map(str, input().split()))
    # ACだった場合
    if query[1] == 'AC':
        if ans_list[int(query[0])] == 0 :
            ans_list[int(query[0])] = 1
            ans += 1
            penalty = penalty + WA_list[int(query[0])]
    # WAだった場合 
    else:
        if ans_list[int(query[0])] == 0 :
            WA_list[int(query[0])] += 1

print("{0} {1}".format(ans, penalty))