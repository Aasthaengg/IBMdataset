a,b,c = map(int,input().split())
res = 0
for i in range(b):
    res =(a * i)% b
    if res == c:
        print("YES")
        break
else:
    print("NO")
