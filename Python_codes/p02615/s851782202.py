
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    asort = sorted(a,reverse=True)
    if n % 2 == 0:
        use = n // 2
        res = sum(asort[:use])*2 - max(asort)
    else:
        use = n // 2 + 1
        res = sum(asort[:use])*2 - max(asort) - min(asort[:use])
    print(res)    