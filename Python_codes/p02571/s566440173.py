s=input()
t=input()
mx=0
for i in range(len(s)-len(t)+1):
    sm=0
    for j in range(len(t)):
        if s[i+j]==t[j]:
            sm+=1
    mx=max(sm,mx)
print(len(t)-mx)