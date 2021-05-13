
n = int(input())

d_list = []
for i in range(n):
    d_list.append(int(input()))

d_list = list(set(d_list))
# イメージのため 問題に回答する上でこの処理は不要
d_list = sorted(d_list, reverse = True)

ans = len(d_list)

print(ans)
