S=input()
m=0
for i in S:
    if i=="x":
        m+=1
if m>=8:
    print("NO")
else:
    print("YES")