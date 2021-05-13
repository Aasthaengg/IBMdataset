s=input()
n=[0,0,0]
for i in range(len(s)):
    if s[i] == "a":
        n[0]+=1
    elif s[i] == "b":
        n[1]+=1
    else:
        n[2]+=1
if abs(n[0]-n[1]) <= 1 and abs(n[1]-n[2]) <= 1 and abs(n[0]-n[2]) <= 1:
    print("YES")
else:
    print("NO")