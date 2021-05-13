X = int(input())
n = 1
while True:
    if n*(n+1)//2 >= X:
        print(n)
        break
    n +=1