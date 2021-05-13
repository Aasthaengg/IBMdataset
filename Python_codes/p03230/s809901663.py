n=int(input())
d=int((1+8*n)**(1/2))
if d**2!=(1+8*n) or d%2==0:
    print("No");exit()
k=(1+d)//2
print("Yes")
print(k)
haba=1
cnt=1
ret=[[] for i in range(k)]
while cnt<=n:
    for s in range(k-haba):
        ret[s].append(cnt)
        ret[s+haba].append(cnt)
        cnt+=1
    haba+=1
for i in ret:
    print(len(i),*i)