lst=[2**i for i in range(0,7)]
lst=sorted(lst,reverse=True)

n=int(input())
for i in lst:
    if i<=n:
        print(i)
        break