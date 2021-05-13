import string

s=list(input())
k=int(input())

str=string.ascii_lowercase
abc=str+str

s_len=len(s)
for i in range(s_len):
  si_inx=abc.index(s[i])

  if i==s_len-1:
    k%=26
    s[i]=abc[si_inx+k]
    break

  if s[i]=='a':
    continue

  if k>=26-si_inx:
    k-=26-si_inx
    s[i]='a'
  else:
    continue

  if k<=0:
    break

print(''.join(s))