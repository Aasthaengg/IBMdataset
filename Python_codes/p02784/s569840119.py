import sys
H,N = map(int,input().split())
array = list(map(int,input().split()))

if not ( 1 <= H <= 10**9 and 1 <= N <= 10**5 ): sys.exit()
if not ( 1 <= min(array) and max(array) <= 10**4 ): sys.exit()

print('Yes') if sum(array) >= H else print('No')