N, T = map(int, input().split())
t = list(map(int, input().split()))

cnt = T
time = T

for i in range(1, N):
    if(t[i] <= time):
        cnt += (t[i]-time)+T
        time = t[i]+T
    else:
        time = t[i]+T
        cnt += T
print(cnt)