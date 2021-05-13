N = int(input())
A = list(map(int,input().split()))

for i in range(1,N+1):
    A[i-1] -= i
sA = sorted(A)

def sadness(b):
    global A
    s = 0
    for i, a in enumerate(A):
        s += abs(a-b)
    return s

print(sadness(sA[len(A)//2]))