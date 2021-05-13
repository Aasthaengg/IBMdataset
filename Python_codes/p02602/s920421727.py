#template
def inputlist(): return [int(j) for j in input().split()]
#template
N,K = inputlist()
A = inputlist()
A = [0]+A
for i in range(1,N-K+1):
    if A[i+K] > A[i]:
        print("Yes")
    else:
        print("No")