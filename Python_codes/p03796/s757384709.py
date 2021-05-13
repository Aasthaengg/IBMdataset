n=int(input())
power=1
mod=10**9+7
for num in range(1,n+1):
    power*=num
    power%=mod
print(power)