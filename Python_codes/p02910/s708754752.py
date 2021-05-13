s=input()

ans="Yes"

#奇数
os=s[::2]
#print(os)
if "L" in os:
    ans="No"


#偶数
es=s[1::2]
#print(es)
if "R" in es:
    ans="No"
    
print(ans)