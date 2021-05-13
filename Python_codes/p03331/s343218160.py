N = int(input())

def wa(x):
    s = 0
    while x > 0:
        s += x % 10
        x = int(x / 10)
    return s
L = []
for i in range(1,N):
    A = i
    B = N - i
    x = wa(A) + wa(B)
    L.append(x)
    
L = sorted(L)
    
print(L[0])