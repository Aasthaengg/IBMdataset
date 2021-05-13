import sys
input = sys.stdin.readline

s = input().rstrip()
l = [0]*len(s)
k=0
for i in range(1,len(s)-1):
    if s[i] == s[i-1] and l[i-1] == 0:
        l[i]=1
        l[i+1]=1
        
if len(s) >1 and s[-1] == s[-2] and l[-2] == 0:
    l[-2] = 1
    l[-1]=1
print(len(s)-sum(l)//2)
