L = [0]*100501
for i in range(6):
    L[100+i] = 1
for i in range(100001):
    if L[i]==1:
        for j in range(6):
            if (L[i+j+100] == 0):
                L[i+j+100] = 1
print(L[int(input())])