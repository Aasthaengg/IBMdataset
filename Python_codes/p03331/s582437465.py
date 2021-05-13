def sum_value(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum+=int(n[i])
    return sum

N = int(input())
A = int(N/2)
B = int(N/2) if N%2 == 0 else int(N/2)+1
menor = -1
for i in range(int(N/2)):
    menor = sum_value(A+i)+sum_value(B-i) if menor < 0 else min(sum_value(A+i)+sum_value(B-i), menor) 
print(menor)