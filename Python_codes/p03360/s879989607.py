import sys
array_abc = list(map(int,input().split()))
K = int(input())

if not ( 1 <= min(array_abc),max(array_abc) <= 50 ):
    sys.exit()
if not ( 1 <= K <= 10 ):
    sys.exit()

print(sum(array_abc) + max(array_abc) * (2 ** K - 1))