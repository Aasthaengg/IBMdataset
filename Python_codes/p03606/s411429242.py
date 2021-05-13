n=int(input())
s = [tuple(map(int,input().split(" "))) for i in range(n)]
ans = 0
for i in s:
    ans += i[1]-i[0]+1
print(ans)