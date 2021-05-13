l = sorted(list(map(int, input().split())))
ans = 0
if l[0]%2!=0 and l[1]%2!=0 and l[2]%2!=0:
    ans += l[0]*l[1]
print(ans)