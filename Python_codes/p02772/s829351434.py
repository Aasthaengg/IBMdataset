n = int(input())
al = list(map(int,input().split()))
bl = []
count = 0
#print(al)

for i in range(len(al)):
    if al[i] %2 == 0:
        bl.append(al[i])

#print(bl)

for j in range(len(bl)):
    
    if bl[j] %3 == 0 or bl[j] %5 == 0:
        count += 1
    else:
        pass
    
print(['DENIED','APPROVED'][count == len(bl)])