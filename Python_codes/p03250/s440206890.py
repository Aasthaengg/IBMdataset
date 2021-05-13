li = list(map(int, input().split()))
ans = 0
li.sort()
ans += li[0]+li[1]+li[2]*10
print(ans)