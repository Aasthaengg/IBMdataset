L = [[] for i in range(5)]

for i in range(2,55556):
    D = 0
    for j in range(2,int(i**(1/2))+1):
        if i % j == 0:
            D = -1
            break
    if D == 0:
        L[i%5].append(i)

#print(L)
#for i in range(5):
#    print(len(L[i]))

N = int(input())
print(" ".join(map(str,L[1][:N])))
