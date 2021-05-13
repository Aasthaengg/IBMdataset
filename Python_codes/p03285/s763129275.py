N = int(input())

#4,7何書いても良い

max_CA = int(N / 4) + int(N % 4) 
max_CB = int(N / 7) + int(N % 7)

#print(f'four:{max_CA}')
#print(f'seven:{max_CB}')

flag = False
for i in range(max_CA +1):
    for j in range(max_CB+1):
        sum_C = 4 * i + 7 * j
        if N == sum_C:
            flag = True
            
if flag:
    print('Yes')
else:
    print('No')
