s,t=input(),input()
ans=len(t)
"""
s[x]から、t文字分探索。tと一致しない箇所があればtmpをプラス。
tmpの合計は直さなくてはいけない文字の数だから、tmpの各合計の中で最も小さい数が答え。
"""
for x in range(len(s)-len(t)+1):
    tmp=0
    for y in range(len(t)):
        if s[x+y]!=t[y]:
            tmp+=1
    ans=min(ans,tmp)        
print(ans)