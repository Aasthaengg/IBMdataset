import sys
N,M,C = map(int,input().split())
array_b = list(map(int,input().split()))
array2_a = [ list(map(int,input().split())) if ( -100 <= I <= 100 ) else sys.exit() for I in range(N) ] 

if not ( 1 <= N <= 20 and 1 <= M <= 20 ): sys.exit()
for J in range(len(array_b)): 
    if not ( -100 <= array_b[J] <= 100 ): sys.exit()

count = 0
for K in range(N):
    sum = 0
    for L in range(len(array2_a[K])):
        sum += array_b[L] * array2_a[K][L]
    if sum + C > 0: count += 1

print(count)