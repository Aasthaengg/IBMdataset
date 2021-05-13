def some():
    n = int(input())
    odds = len([i for i in range(1, n+1) if i%2 != 0])
    print(odds/n)
some()