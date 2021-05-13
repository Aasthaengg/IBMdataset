s=list(input())
t=list(input())

if not "?" in s:
    if ("".join(t) in "".join(s)):
        print("".join(s))
    else:
        print("UNRESTORABLE")
    exit()

ans=[]
switch=1
p=len(s)-len(t)
for i in range(p+1):
    for j in range(len(t)):
        if s[j+i]!=t[j] and s[j+i]!="?":
            switch=0
    if switch==1:
        c_s=s[:]
        for j in range(len(t)):
            c_s[j+i]=t[j]
        for j in range(len(c_s)):
            if c_s[j]=="?":
                c_s[j]="a"
        ans.append("".join(c_s))
    switch=1

if len(ans)==0:
    print("UNRESTORABLE")
else:
    ans.sort()
    print(ans[0])