from fractions import Fraction

N,K=map(int,input().split())

case = []
number = []
count = 0
result_a = 0

for i in range(N):
    case.append(i+1)

for j in range(N):
    while case[j] <= K-1:
        case[j] *= 2
        count += 1
    count = 2**count
    number.append(count*N)
    count = 0

for k in range(N):
    number[k] = Fraction(1,number[k])

for l in range(N):
    result_a += number[l]

result_b = float(result_a)
print(result_b)