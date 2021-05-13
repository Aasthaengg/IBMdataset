n,k = map(int,input().split())
l = [int(i) for i in input().split()]
l_new= sorted(l,reverse=True)
ans = sum(l_new[:k])
print(ans)