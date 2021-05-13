n=int(input())
a=[2**i for i in range(6,-1,-1)]
for i in a:
    if n>=i:
        print(i)
        break