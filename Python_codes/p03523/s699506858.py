#1
#入力
S=input()


#処理
import re
m=re.fullmatch(r'A?KIHA?BA?RA?',S)

if m==None:
    print("NO")
else:
    print("YES")
