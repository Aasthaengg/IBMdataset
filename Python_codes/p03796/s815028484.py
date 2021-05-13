import sys
N = int(input())
if N < 0 or N > 100000:
    sys.exit()
power = 1
for I in range(1,N+1):
    # print("power="+str(power))
    # print("I="+str(I))
    power = power * I % (10**9+7)

print(power)