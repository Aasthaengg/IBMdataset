s= input().strip()
t= input().strip()

ls=len(s)
lt=len(t)
v=''
for i in range(lt):
    v+=s[i]+t[i]
if lt!=ls:
    v+=s[-1]
print(v)