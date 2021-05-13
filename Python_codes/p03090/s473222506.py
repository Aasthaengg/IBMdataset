n = int(input())
x = n % 2

ans = []
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if x == 0:
            if i == n+1-j:
                continue
            ans.append((i,j))
        else:
            if i == (n-j):
                continue
            ans.append((i,j))
            
print(len(ans))
for i in ans:
    print(*i)