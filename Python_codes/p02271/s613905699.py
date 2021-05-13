import sys
sys.setrecursionlimit(100000)  # set the maximum depth as 10000

n=int(input())
A=[int(x) for x in input().split()]
minA=min(A)
sumA=0
for i in A:
    sumA+=i
    


q=int(input())
M=[int(x) for x in input().split()]


def solve(i,m):
    global n
    global A
    global minA
    global sumA
    
    if m<0 or m>sumA:
        return False
    if m==0:
        return True
    if i>=n:
        return False
    
    return solve(i+1,m) or solve(i+1,m-A[i])
    
    
for m in M:
    if m<minA or m>sumA:
        print('no')
    else:
        if solve(0,m):
            print('yes')
        else:
            print('no')
