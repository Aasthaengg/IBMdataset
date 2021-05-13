s=input()
mod=10**9+7
a=0
ab=0
abc=0
q=1
for i in s:
    if i=="?":
        abc*=3
        abc+=ab
        ab*=3
        ab+=a
        a*=3
        a+=q
        q*=3
        q%=mod
    elif i=="A":
        a+=q
    elif i=="B":
        ab+=a
    else:
        abc+=ab
    abc%=mod
    ab%=mod
    a%=mod
print(abc)