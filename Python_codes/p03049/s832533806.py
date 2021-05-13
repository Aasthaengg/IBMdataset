n = int(input())
s = []
for i in range(n):
    s.append(input())
out = 0
a=0
b=0
c=0
for i in range(len(s)):
    if s[i][0] == "B" and s[i][len(s[i])-1] == "A":
        a=a+1
    elif s[i][0] == "B" and s[i][len(s[i])-1] != "A":
        b=b+1
    elif s[i][0] != "B" and s[i][len(s[i])-1] == "A":
        c=c+1
    for j in range(len(s[i])-1):
        if s[i][j] == "A" and s[i][j+1] == "B":
            out = out+1
if a== 0 and b == 0 and c == 0:
    out = out
elif b == 0 and c == 0:
    out = out + a - 1
else :
    out = out +a+ min(b,c)
    
print(int(out))