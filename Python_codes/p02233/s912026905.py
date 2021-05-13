lis=[]
lis.append(1)
lis.append(1)
for i in range(2,45):
    lis.append(lis[i-1]+lis[i-2])

n = int(input())
print(lis[n])

