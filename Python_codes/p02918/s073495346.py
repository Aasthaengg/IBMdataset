n,k = map(int,input().split())
s = input()
ls =[]
p = s[0]
cnt = 1
for i in range(1,n):
    if p != s[i]:
        ls.append((p,cnt))
        cnt = 0
    cnt += 1
    p = s[i]
ls.append((p,cnt))

l = len(ls)
ans = 0
for i in range(k):
    idx = 2*i+1
    if idx >l-1:break
    if idx == l-1:
        ans+=1
        break
    ans +=2
for w,c in ls:
    ans+=c-1
print(ans)
