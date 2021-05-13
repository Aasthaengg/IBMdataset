while True:
    n=input()
    if n=='0':
        break
    s=list(n)
    a=[int(i) for i in s]
    print(sum(a))
