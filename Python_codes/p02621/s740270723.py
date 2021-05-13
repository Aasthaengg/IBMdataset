#!/usr/bin/python3
 
cmdvar_N=int(input())
tmp=cmdvar_N
for i in 2,3:
    tmp=tmp+cmdvar_N**i

print(tmp)