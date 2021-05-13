K = int(input())

gu = 0
for i in range(1,K+1):
    if i % 2 ==0:
        gu+=1

ki = 0
for j in range(1,K+1):
    if j % 2 ==1:
        ki+=1

print(gu*ki)