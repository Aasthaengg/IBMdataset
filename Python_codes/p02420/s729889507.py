while True:

    a=input()
    if a=="-":
        break

    N=int(input())
    for i in range(N):
        n=int(input())
        a=a[n:]+a[:n]

    print(a)
