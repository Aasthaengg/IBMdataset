s =input()
n = len(s)
ans  = 0
cnt = 0
pre = s[0]
for i in range(n):
    if s[i] == "A":
        if pre =="B":cnt =1
        else:cnt+=1
    elif s[i] =="C":
        if pre == "B":
            ans += cnt
        else:cnt = 0
    elif s[i] == "B":
        if pre == "B":cnt = 0
    pre = s[i]
print(ans)
