N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def check(A,B):
    plus,minus = 0,0
    for i in range(N):
        diff = B[i]-A[i]
        if diff>0:
            plus += diff//2
        else:
            minus -= diff
    if plus >= minus:
        return True
    return False 

if check(A,B):
    print('Yes')
else:
    print('No')