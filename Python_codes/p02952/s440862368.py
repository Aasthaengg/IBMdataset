import sys
str_N = input()
N = int(str_N)

if not ( 1 <= N <= 10**5 ): sys.exit()

count = 0
for I in range(1,N+1):
    if len(str(I)) % 2 == 1: count += 1
print(count)