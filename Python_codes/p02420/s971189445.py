while True:
    a=input()
    if a=='-':
        break
    else:
        n=int(input())
        for i in range(n):
             h=int(input())
             a=a[h:]+a[:h]
    print(a)