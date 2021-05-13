n=int(input())
a=0
b=0
ab=0
num=0
for i in range(n):
    s=input()
    if s[0]=="B" and s[-1]=="A":
        ab+=1
    elif s[0]=="B":
        b+=1
    elif s[-1]=="A":
        a+=1
    for j in range(len(s)-1):
        if s[j]=="A" and s[j+1]=="B":
            num+=1
if a!=0 and b!=0:
    num+=ab+1
    a-=1
    b-=1
    num+=min(a,b)
elif a!=0:
    num+=ab
elif b!=0:
    num+=ab
else:
    num+=max(0,ab-1)
print(num)
