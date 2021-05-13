# AtCoder Beginner Contest 052 - A
# -*- encoding: UTF-8 -*-
a,b,c,d = map(int, input().split())

t1 = a * b
t2 = c * d

if t1 < t2 :
   print(t2)
else :
   print(t1)
