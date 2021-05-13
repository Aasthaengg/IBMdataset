# -*- coding: utf-8 -*-
 
# Input
s = [input() for i in range(2)]
 
N = int(s[0].split()[0])
A = int(s[0].split()[1])
B = int(s[0].split()[2])
X = s[1].split()
 
F = 0
 
# 疲労度の少ない方法を逐次選択する
for i in range(0, N-1):
    if A*(int(X[i+1]) - int(X[i])) >= B:
        F = F + B
    else:
        F = F + A*(int(X[i+1]) - int(X[i]))
 
# Output
print(F)