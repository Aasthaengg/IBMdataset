N,K =map(int,input().split())
li = list(map(int,input().split()))

li.sort(reverse=True)
ans = sum(li[0:K])
print(ans)