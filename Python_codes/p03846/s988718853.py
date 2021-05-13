n = int(input())
q = [int(x) for x in input().split(' ')]
q_set = set(q)

if (n%2 == 1):
    count = 2**((n-1)//2)
else:
    count = 2**(n//2)
    
    
if (sum(q) == 2*sum(q_set)):
    print(count%(10**9+7))
else:
    print(0)