n , m = map(int,input().split())
ans = [1 for i in range(n)]
for i in range(m):
    a , b = map(int,input().split())
    if a != 1:
        ans[a-1] *= -1
    if b != 1:
        ans[b-1] *= -1
        
for i in ans:
    if i == -1:
        print("NO")
        exit()
print("YES")