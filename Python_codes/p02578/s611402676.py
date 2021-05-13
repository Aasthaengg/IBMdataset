N = int(input(''))
A = input('')
a_n = A.split()
A_N = list(map(int, a_n))
num = 0 
for i in range(1,N):
    if A_N[i] >= A_N[i-1]:
        num += 0
    elif A_N[i] < A_N[i-1]:
        num += A_N[i-1] - A_N[i]
        A_N[i] = A_N[i-1]
print(num)