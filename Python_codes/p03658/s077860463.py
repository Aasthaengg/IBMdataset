N,M = map(int,input().split())
L = sorted(map(int,input().split()),reverse=True)

sum = 0
for i in range(M):
    sum += L[i]

    
print(sum)