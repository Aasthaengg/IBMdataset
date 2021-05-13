import math
N1 = input()
N = int(N1)
i = 0
j = 1
r = 0
a = 0
for j in range (N):
    i=N-j
    if i!=j : 
        r+=1
        
a = math.floor (r/2)
print(a)