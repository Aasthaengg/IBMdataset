import math 

divisor = (10 ** 9) + 7

N, M = [int(i) for i in input().split()]

output = 0

n_fact = math.factorial(N) 
m_fact = math.factorial(M) 

diff = abs(N-M)

if diff == 0 :
    output = n_fact * m_fact * 2 % divisor
elif diff == 1:
    output = n_fact * m_fact % divisor 

print(output)