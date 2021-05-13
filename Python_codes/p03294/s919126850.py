#template
def inputlist(): return [int(k) for k in input().split()]
#template
N = int(input())
A = inputlist()
print(sum(A)-N)