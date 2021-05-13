n = int(input())

x = list(map(int,input().split()))

y = sorted(x)

for i in x:
    if y[(n+1)//2-1] >= i:
        print(y[(n+1)//2])
    else:
        print(y[(n+1)//2-1])