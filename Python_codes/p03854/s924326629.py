s=list(reversed(list(input())))
n=len(s)
for i in range(6):
    s.append("#")
d=0
f=0
while f==0 and s[d]!="#":
    if s[d]+s[d+1]+s[d+2]+s[d+3]+s[d+4]=="maerd":
        d+=5

    elif s[d]+s[d+1]+s[d+2]+s[d+3]+s[d+4]+s[d+5]+s[d+6]=="remaerd":
        d+=7

    elif s[d]+s[d+1]+s[d+2]+s[d+3]+s[d+4]=="esare":
        d+=5
    elif s[d]+s[d+1]+s[d+2]+s[d+3]+s[d+4]+s[d+5]=="resare":
        d+=6
    else:
        f=1
print("YES" if f==0 else "NO")


