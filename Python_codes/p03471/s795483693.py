n,y=map(int, input().split())
nums=[i for i in range(n+1)]
judge = 0
for i in range(n+1):
    for j in range(n+1-i):
        price = i * 10000 + j * 5000 + (n-i-j) * 1000
        if y == price:
            judge += 1
            print(str(i) + " " + str(j) + " " + str(n-i-j))
            break
    if judge == 1:
        break
if judge == 0:
    print("-1 -1 -1")