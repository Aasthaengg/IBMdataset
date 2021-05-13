input()
A = list(map(int,input().split()))
input()
M = list(map(int,input().split()))

def makeSum(A,i,T):
    if i == len(A):
        T[sum(A)] = 0
    else:
        makeSum(A,i+1,T)
        ret = A[i]
        A[i] = 0
        makeSum(A,i+1,T)
        A[i] = ret

T = {}
makeSum(A,0,T)
for m in M:
    if m in T:
        print("yes")
    else:
        print("no")