a = list(map(int, input().split()))

num00 = a[3]-a[1]
num01 = a[2]-a[0]
ans = ['U']*num00
ans += ['R']*num01
ans += ['D']*num00
ans += ['L']*num01

ans += ['L']
ans += ['U']*(num00+1)
ans += ['R']*(num01+1)
ans += ['D']

ans += ['R']
ans += ['D']*(num00+1)
ans += ['L']*(num01+1)
ans += ['U']

print(*ans, sep='')
