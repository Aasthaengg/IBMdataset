s=input()
n=len(s)
for i in range(n):
    if s[i]=="A":
        start=i
        break
for i in range(n):
    if s[i]=="Z":
        goal=i
ans=goal-start
print(ans+1)