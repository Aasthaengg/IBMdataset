def abc136c():
    n = int(input())
    h = list(map(int, input().split()))
    v = 0
    for i in range(n):
        if v > h[i]:
            print('No')
            return
        v = max(v, h[i]-1)
    print('Yes')
abc136c()