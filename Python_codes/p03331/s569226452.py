N=int(input())

def digitsum(x):
    res=0
    while x>0:
        res+=x%10
        x//=10
    return res

counter=90
for A in range(1,N):
    if digitsum(A)+digitsum(N-A)<counter:
        counter=digitsum(A)+digitsum(N-A)

print(counter)
