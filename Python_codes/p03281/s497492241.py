n = int(input())
ans = 0
for i in range(1,n+1):
    c = 0
    for j in range(1,201,2):
        c += i%j == 0
    ans += c == 8
print(ans)
