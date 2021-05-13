#coding:utf-8
S=raw_input()

all=1
a=ab=abc=0
MOD=(10**9)+7
for _ in range(len(S)):
    i=_+1
    c=S[_]
    if c=="A":
        a+=all
    if c=="B":
        ab+=a
    if c=="C":
        abc+=ab
    if c=="?":
        abc=abc*3+ab
        ab=ab*3+a
        a=a*3+all
        all*=3
    a%=MOD
    ab%=MOD
    abc%=MOD
    all%=MOD
print(abc%((10**9)+7))

    












