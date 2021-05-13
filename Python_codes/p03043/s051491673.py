from fractions import Fraction

N,K=map(int,input().split())

number = []
count = 0
result_a = 0

for i in range(1,N+1):
    while i <= K-1:
        i *= 2
        count += 1
    count = 2**count
    number.append(count*N)
    count = 0

for j in range(N):
    number[j] = Fraction(1,number[j])

for k in range(N):
    result_a += number[k]

result_b = float(result_a)
print(result_b)