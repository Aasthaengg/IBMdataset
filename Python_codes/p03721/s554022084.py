N, K = map(int, input().split())

L = []
for i in range(10**5+1):
    L.append(0)

for n in range(N):
    a, b = map(int, input().split())
    L[a] += b

a = 0
while K > 0:
    a += 1
    K -= L[a]
    
print(a)