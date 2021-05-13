#https://atcoder.jp/contests/abc153/tasks/abc153_b
S_list = [(input()) for i in range(2)]
H,N = map(int,S_list[0].split())
S_list_1 = list(map(int,S_list[1].split()))
damage = sum(S_list_1)
if damage >= H:
    result = "Yes"
else:
    result = "No"
print(result)