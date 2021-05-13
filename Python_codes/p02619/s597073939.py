# coding: utf-8
# Your code here!

d= int(input())

C = list(map(int,input().split()))
CB = [0 for i in range(len(C))]

c = sum(C)

total = 0

#print(c,C,CB)
L = []

for i in range(d):
    L.append(list(map(int,input().split())))

#print(L)

T = []

for i in range(d):
    T.append(int(input()))

#print(T)

def cnt(CB,t):
    for i in range(len(CB)):
        if i != t-1:
            CB[i] += 1
        else:
            CB[i] = 0
    
    return CB

def sumA(C,CB):
    a = 0
    for i in range(len(CB)):
        a += CB[i]*C[i]
    return a

for i in range(len(T)):
    CB = cnt(CB,T[i])
    total += L[i][T[i]-1] - sumA(C,CB)
    print(total)



