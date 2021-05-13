import math
import copy

neko = 0
nuko = 0
a,b = map(int,input().split())
for i in range(a,b+1):
    s1 = i//10000
    s2 = (i%10000)//1000
    s3 = (i%100)//10
    s4 = i%10
    if (s1 == s4)and(s2 == s3):
        neko += 1
print(neko)