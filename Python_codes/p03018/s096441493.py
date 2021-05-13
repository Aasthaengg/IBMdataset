s = input().strip()
x = [s[0]]
for i in range(1,len(s)):
    if s[i]=="C" and s[i-1]=="B":
        x.pop()
        x.append("T")
    else:
        x.append(s[i])
cnt = 0
ca = 0
for i in range(len(x)):
    if x[i]=="A":
        ca += 1
    elif x[i]=="T":
        cnt += ca
    elif x[i]=="B" or x[i]=="C":
        ca = 0
print(cnt) 