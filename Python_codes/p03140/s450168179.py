# coding: utf-8
# Your code here!

N = int(input())

w = [input() for i in range(3)]

c = 0

for i in range(N):
    if w[0][i]!=w[1][i]:
        c += 1
    
    if (w[0][i]!=w[2][i]) and (w[1][i]!=w[2][i]):
        c += 1

print(c)

