n = int(input())
ans = 10000000
for i in range(1,n):
    x = sum(list(map(int,str(i))))+sum(list(map(int,str(n-i))))
    if x <= ans:
        ans = x
print(ans)