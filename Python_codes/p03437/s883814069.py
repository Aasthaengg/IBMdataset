X, Y = map(int, input().split())
 
if X % Y:
    for i in range(2, 10**9):
        if X * i % Y:
            print(X * i)
            break
else:
    print(-1)