n,a,b,c=map(int,input().split())
bam=[]
for i in range(n):
  bam.append(int(input()))
def base10toN(num, base):
    converted_string, modstring = "", ""
    currentnum = num
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string
ans=10**18
for i in range(4**n):
  s=base10toN(i, 4)
  slist=[]
  for i in range(len(s)):
    slist.append(s[i])
  slist.reverse()
  for i in range(n-len(s)):
    slist.append('0')
  slist.reverse()
  s1=[]
  s2=[]
  s3=[]
  for i in range(n):
    if slist[i]=='1':
      s1.append(bam[i])
    if slist[i]=='2':
      s2.append(bam[i])
    if slist[i]=='3':
      s3.append(bam[i])
  if len(s1)==0 or len(s2)==0 or len(s3)==0:
    continue
  anscan=abs(sum(s1)-a)+abs(sum(s2)-b)+abs(sum(s3)-c)+10*(len(s1)-1)+10*(len(s2)-1)+10*(len(s3)-1)
  ans=min(ans,anscan)
print(ans)