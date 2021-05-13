a,b,c=map(int,input().split())
l=[a,b,c]
l.sort()
cnt=l[2]-l[1]
sa=l[2]-(l[0]+cnt)
cnt+=sa//2
if sa%2!=0:
  cnt+=2
print(cnt)