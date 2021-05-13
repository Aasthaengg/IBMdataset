N,X=map(int,input().split())
p=0
cnt=1
for i in map(int,input().split()):
 p+=i
 if (X<p):break
 cnt+=1
print(cnt)