a,b=map(int,input().split())
s=input()
inter = s[b-1]
inter_new = inter.lower()
res = ""
if b ==1:
  res = inter_new+s[1:len(s)]
elif b == a:
  res = s[0:len(s)-1]+inter_new
else:
  res = s[0:b-1]+inter_new+s[b:len(s)]
print(res)