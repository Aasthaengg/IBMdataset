N=input()
import re
if re.match('10+',N):
    print(10)
else:
    ans=0
    for n in N:
        ans+=int(n)
    print(ans)