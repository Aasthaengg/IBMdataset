N = int(input())
kyc8 = 0
for i in range(1,N+1,2):
    yc = 0
    for j in range(1,i+1):
        if i % j == 0:
            yc += 1
    if yc == 8:
        kyc8 += 1
print(kyc8)