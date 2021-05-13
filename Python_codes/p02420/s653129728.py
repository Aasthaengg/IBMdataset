while True:
    N=input()
    if N=="-":
        break
    K=int(input())
    su=0
    for i in range(K):
        J=int(input())
        su+=J
    su=su%len(N)
    formar=N[:su]
    later=N[su:]
    print(later+formar)
