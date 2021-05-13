 
import re
 
 
S = input()
 
if re.fullmatch(r"A?KIHA?BA?RA?",S):
    print("YES")
else:
    print("NO")
exit()