from sys import stdin,stdout
for _ in range(1):#int(stdin.readline())):
    n=int(stdin.readline());p=1
    # n,k=map(int,stdin.readline().split())
    a=list(map(int,stdin.readline().split()))
    if 0 in a:
        print(0)
        exit(0)
    for v in a:
        p*=v
        if p>(10**18):
            p=-1
            break
    print(p)