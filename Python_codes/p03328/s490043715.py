a,b = map(int,input().split())

temp = 0
dif = b - a

for i in range(1,1000):
    temp += i
    if i == dif:
        ans = temp - b
        print(ans)
        exit(0)