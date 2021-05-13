N, T = map(int, input().split())
t_list = list(map(int, input().split()))
cnt = T
for i in range(1, N):
    cnt += T
    if t_list[i]-t_list[i-1]<=T:
        cnt -= T-(t_list[i]-t_list[i-1])
print(cnt)