N=int(input())
power=1
for i in range(N):
    power=power*(i+1)
    power=power%(10**9+7)

print(power)
