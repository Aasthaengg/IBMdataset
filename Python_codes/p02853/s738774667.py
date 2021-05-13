n = [int(i) for i in input().split()]
T=0
for i in range(2):
        if n[i] == 1: T+=3
        elif n[i] == 2: T+=2
        elif n[i] == 3: T+=1
if sum(n)==2: T+=4
print(T*100000)