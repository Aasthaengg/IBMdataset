## coding: UTF-8
s = input().split()
t = [int(p) for p in s]
#print(t)

N = t[0]
K = t[1]

answer = K * ((K-1) ** (N-1))
print(answer)