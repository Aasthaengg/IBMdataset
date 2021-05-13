#template
def inputlist(): return [int(k) for k in input().split()]
#template
N,K = inputlist()
if K == 1:
    print(0)
else:
    print(N-K)