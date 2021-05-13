K,X = map(int,input().split())
ans = ''
for i in range(-(K-1),K-1) :
    ans += str(X+i) + ' '

ans += str(X+(K-1))
print(ans)