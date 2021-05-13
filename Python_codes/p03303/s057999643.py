from math import ceil
S=input()
w=int(input())
s=""
for i in range(len(S)):
    if i%w==0:
        s="".join((s,S[i]))
print(s)
