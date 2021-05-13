def abc172d():
    n = int(input())
    total = 0
    for i in range(1, n+1):
        total += (i+n//i*i)*((n//i)/2)
    print(int(total))
abc172d()