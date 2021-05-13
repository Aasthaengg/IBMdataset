#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,A,B,C,D = map(int,input().split())
s = list(input())
ok = False

# AC間、BD間、に連続した岩がなければ良い
#print (s)
for i in range(A-1,C):
#    print (s[i-1:i+1])
    if s[i-1:i+1] == ["#","#"]:
        print ("No")
        exit ()

#print (s)
for i in range(B-1,D):
#    print (s[i-1:i+1])
    if s[i-1:i+1] == ["#","#"]:
        print ("No")
        exit ()


# C > D の場合
# BD間に連続した3つの空きがあれば良い
if C < D:
    ok = True
else:
#    print (s)
    for i in range(B-1,D):
#        print (s[i-1:i+2])
        if s[i-1:i+2] == [".",".","."]:
            ok = True
            break

if ok:
    print ("Yes")
else:
    print ("No")
