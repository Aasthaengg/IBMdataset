n,m = map(int,input().split())
s = [0]*(n)
for i in range(m):
    a,b = map(int,input().split())
    s[a-1] += 1
    s[b-1] += 1
for i in s:
    if i%2 != 0:
        print("NO")
        exit()
print("YES")