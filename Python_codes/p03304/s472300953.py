n, m, d = map(int,input().split())
if d == 0:
    prob = 1/n
    print(prob*(m-1))
    exit()

else:
    prob = (2*(n-d))/(n**2)
    print(prob*(m-1))
