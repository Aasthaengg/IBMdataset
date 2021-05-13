import sys
sys.setrecursionlimit(10**6)

s=list(input())
n=len(s)

#print(s[0],s[1])

cnt0=0
cnt1=0
for i in range(n):
    if s[i]=="0":
        cnt0+=1
    elif s[i]=="1":
        cnt1+=1

print(2*min(cnt0,cnt1))
