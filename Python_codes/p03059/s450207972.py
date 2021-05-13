import sys
A,B,T = map(int,input().split())
if not ( 1 <= A <= 20 and 1 <= B <= 20 and 1 <= T <= 20 ): sys.exit()

time_remind = T+0.5
sum = 0
for I in range(1,T+1):
    time_remind -= A
    if time_remind >= 0: sum += B
print(sum)