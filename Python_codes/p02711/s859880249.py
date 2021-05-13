# 162 A
N = int(input())
A = int(N/100)
B = str(N)[1:2]
C = N%10
ans = [A,int(B),C]
print('Yes') if 7 in ans else print('No')