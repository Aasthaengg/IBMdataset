n,y = map(int, input().split())

y //= 1000

for i in range(0,y+1,5):
    for j in range(0,i+1,10):
        a,b,c = j,i-j,y-i
        a //= 10
        b //= 5
        if a+b+c == n:
            print(a,b,c)
            exit()
print(-1,-1,-1)