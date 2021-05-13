A_interval, B_mai, T_limit = map(int, input().split())

times = T_limit // A_interval

ans = B_mai * times
print(ans)