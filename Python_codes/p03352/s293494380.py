X = int(input())

dammy=[]
for b in range(1,101):
    for p in range(2,10):
        dammy.append(b**p)
        dammy.sort()

for i in range(101):
    if dammy[i]>X:
        print(dammy[i-1])
        break