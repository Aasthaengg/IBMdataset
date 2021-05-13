n = int(input())
list_score = [ list(map(int,input().split(" "))) for i in range(n)]
ans = 0
for i,j in list_score:
    ans += j-i+1
print(ans)