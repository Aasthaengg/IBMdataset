import sys

input = sys.stdin.readline

N, T= map(int, input().split())
t_list = list(map(int, input().split()))

ans = T
for i in range(N-1):
    if t_list[i+1] - t_list[i] > T:
        ans += T
    else:
        ans += T - (T - (t_list[i+1] - t_list[i]))
print(ans)