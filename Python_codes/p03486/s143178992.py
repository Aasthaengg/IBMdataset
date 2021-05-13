s=str(input())
t=str(input())

l="abcdefghijklmnopqrstuvwxyz"

ss=''.join(sorted(s))
st=''.join(sorted(t))
str=''.join(sorted(t,reverse=True))

if l.index(str[0])>l.index(ss[0]):
  ans="Yes"
elif len(t)>len(s) and ss in st:
  ans="Yes"
else:
  ans="No"
  
print(ans)
