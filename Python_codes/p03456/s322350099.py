#B - 1 21
a,b = map(str,input().split())

N = a + b
N_number = int(N)#11<=N<=100100

result = 'No'
for i in range(1,N_number // 2):
    if i **2 == N_number:
        result = 'Yes'
print(result)