#A
S=input()
L=["SUN","MON","TUE","WED","THU","FRI","SAT"]
for i in range(7):
    if L[i]==S:
        ans=7-i
print(ans)