N,T = list(map(int,input().split()))
t_list = list(map(int,input().split()))

total = 0
for i in range(N-1):
    total += min(t_list[i+1] - t_list[i], T)
total += T
print(total)