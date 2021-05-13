from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=10**19
###############################################################################\n=17
s=input()
t=input()
ans=10**6
for i in range(len(s)-len(t)+1):
    count=0
    for j in range(len(t)):
        if s[i+j]!=t[j]:
            count+=1
    ans=min(count,ans)
print(ans)
