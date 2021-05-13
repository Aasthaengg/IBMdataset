n, y = map(int, input().split())

for sen in range(0,n+1):
    for go in range(0,n+1):
        if 1000*sen + 5000*go + 10000*(n-sen-go) == y and n-sen-go >= 0:
            print("{} {} {}".format(n-sen-go, go, sen))
            exit()

print("-1 -1 -1")
