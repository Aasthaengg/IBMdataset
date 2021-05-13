s=input()
n=len(s)
t=0
for i in range(n):
    if s[i]=="1":
        t+=1
print(min(2*t,2*(n-t)))