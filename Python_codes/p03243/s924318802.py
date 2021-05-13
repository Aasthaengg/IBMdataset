l=[111*i for i in range(1,10)]
n=int(input())
for i in range(n,1000):
    if n in l:
        print(n)
        exit()
    else:
        n+=1