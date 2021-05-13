N,A,B=map(int,input().split())
souryou=0
for i in range(N):
  j=i+1
  j_str=str(j)
  goukei=0
  for k in range(len(j_str)):
    goukei=goukei+int(j_str[k])
  if goukei>=A and goukei<=B:
    souryou=souryou+j
print(str(souryou))