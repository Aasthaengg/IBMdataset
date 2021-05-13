def main():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    c = 0
    for i in range(N):
        if x >= a[i]:
            x -= a[i]
            c += 1
        else:
            print(c)
            return
    if x > 0:
        print(N-1)
    else:
        print(N)
        
main()