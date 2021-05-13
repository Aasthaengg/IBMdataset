import itertools
import math
n = int(input())
x = [0]
y = [0]
for i in range(1,n+1):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
    
num_list = [int(i) for i in range(1,n+1)]
keiro = []
for v in itertools.permutations(num_list, n):
    keiro.append(list(v))
kensu = math.factorial(n)
#print(keiro)
#print(kensu)
ans = 0
for i in range(kensu):
    for j in range(n-1):
        ans += math.sqrt((x[keiro[i][j]]-x[keiro[i][j+1]])**2+(y[keiro[i][j]]-y[keiro[i][j+1]])**2)
print(ans/kensu)