n,m =map(int, input().split())
    #idxへの行き方の通りをリスト化
num_list = [0]*(n+1)
num_list[0] = 1
a_list =set([int(input()) for _ in range(m)])
if 1 not in a_list:
    num_list[1] = 1
for i in range(2,n+1):
    if i not in a_list:
        num_list[i] = num_list[i-1] + num_list[i-2]
print(num_list[n]%(10**9+7))