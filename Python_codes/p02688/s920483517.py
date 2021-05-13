def main():
    n,k = map(int, input().split())
    i = []
    nn = []
    for d in range(n):
        nn.append(0)

    for kk in range(k):
        kn = int(input())
        s = list(map(int,input().strip().split()))
        for kk in range(kn):
            nn[s[kk] - 1] += 1
    
    c = 0
    for ni in nn:
        if ni == 0:
            c += 1
    
    print(c)
    return 

main()
