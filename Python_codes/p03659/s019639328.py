from itertools import accumulate
N = int(input())
A = [int(i) for i in input().split()]
tmp = list(accumulate(A))[:len(A)-1]
total  = sum(A)

    
ans = min([abs(total-2*a) for a in tmp])
print(ans)