import math
 
S = []
L = []
for i in range(5):
    D = int(input())
    T = math.ceil(D/10)
    S.append(T)
    L.append(T-D/10)
 
print(int((sum(S) - max(L))*10))