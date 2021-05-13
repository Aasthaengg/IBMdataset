s=list(input())
t=list(input())
m=len(t)
for i in range(len(s)-len(t)+1):
    ma=len(t)
    for j in range(len(t)):
        if s[i+j]==t[j]:
            ma-=1
    if ma <m:
        m=ma
print(m)