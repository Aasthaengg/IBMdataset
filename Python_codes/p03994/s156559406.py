s = list(input())
k = int(input())
for i in range(len(s)):
  if ord("z")<ord(s[i])+k and s[i]!="a":
    k =k-(ord("z")-ord(s[i])+1)
    s[i]="a"
  if i==len(s)-1 and 0<k:
    k=k%26
    s[i]=chr(ord(s[i])+k)
print("".join(s))