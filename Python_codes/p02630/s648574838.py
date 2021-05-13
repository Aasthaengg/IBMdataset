n=int(input())
a=list(map(int,input().split()))
q=int(input())
dic = {}
ans = 0
for  x in a:
    if  x not in dic:
        dic[x] = 1
    else:
        dic[x]+=1
    ans += x

for _ in range(q):
    b,c=map(int,input().split())
    if b not in dic:
        print(ans)
        continue
    ans += (c-b)*dic[b]
    if c not in dic:
        dic[c] = dic[b]
    else:
        dic[c]+=dic[b]
    dic[b]=0
    print(ans)