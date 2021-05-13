n, m = map(int,input().split())
num = [0 for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    num[a-1] += 1
    num[b-1] += 1

for i in num:
    if i%2 == 1:
        print("NO")
        exit()

print("YES")
