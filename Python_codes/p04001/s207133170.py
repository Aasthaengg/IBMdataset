S = input()

# TODO: 再帰関数でリストを作成 [s1, "+", s2, s3, "+", s4]とか
result = []
def dfs(i, list):
    if i == len(S):
        result.append(list)
        return
    else:
        if i == len(S) - 1:
            return dfs(i+1, list+[S[i]])
        else:
            return dfs(i+1, list+[S[i]]), dfs(i+1, list+[S[i], "+"])

# TODO: リストに従って和を計算
dfs(0, [])
ans = 0
for l in result:
    sum_of_l = 0
    sequence = 0
    for id in range(len(l)):
        if l[id] == "+":
            sum_of_l += sequence
            sequence = 0
        else:
            sequence *= 10
            sequence += int(l[id])
    sum_of_l += sequence
    ans += sum_of_l

print(ans)
