li = list(map(int, input().split()))
li.sort()
ans = 0
ans += li[2]-li[0]
print(ans)