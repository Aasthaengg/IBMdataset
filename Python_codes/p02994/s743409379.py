n, l = map(int, input().split())
ans = [l + i - 1  for i in range(1,n+1)]

if (l >= 0):
    ans.pop(0)
    print(sum(ans))
elif(n > abs(l)):
    ans.pop(ans.index(0))
    print(sum(ans))
else:
    ans.pop(ans.index(max(ans)))
    print(sum(ans))