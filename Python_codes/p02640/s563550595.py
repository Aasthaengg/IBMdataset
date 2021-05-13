def crane_and_turtle():
    X, Y = map(int, input().split())
    res = "No"
    for i in range(X+1):
        if 4*i + 2*(X-i) == Y:
            res = "Yes"
            break
    print(res)
    
crane_and_turtle()