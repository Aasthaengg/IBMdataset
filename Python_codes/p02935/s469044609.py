N = int(input())
v = list(map(int, input().split()))
v = sorted(v)


L = []
L.append(v[0])
ANS = 0
for i in range(N-1):
    N = (L[i] + v[i+1])/2
    L.append(N)
    
print(max(L))