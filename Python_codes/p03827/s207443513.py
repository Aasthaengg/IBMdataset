n=int(input())
s=input()
t=0
m=0
for x in s:
    if x=='I': t+=1
    else: t-=1
    m = max(m, t)
print(max(m, 0))