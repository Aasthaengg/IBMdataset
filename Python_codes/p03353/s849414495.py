s=input()
k=int(input())
cnt = 0
ans = set([])
head  = sorted(list(set(list(s))),reverse=True)
while cnt < k:
    tmp_h = head.pop()
    for n,i in enumerate(s):
        if i==tmp_h:
            for j in range(min(k,len(s)-n)):
                ans.add(s[n:n+j+1])
    cnt = len(ans)
ans = sorted(list(ans))
print(ans[k-1])