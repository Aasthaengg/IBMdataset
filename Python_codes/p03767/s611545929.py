N = int(input())
power_list = sorted(list(map(int, input().split())), reverse=True)

power = 0
for i in range(N):
  power += power_list[2*i+1]

print(power)