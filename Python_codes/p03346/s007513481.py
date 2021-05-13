#N, *a = map(int, open(0).read().split())
def main():
    N = int(input())
    a=[]
    for i in range(N):
        a.append(int(input()))

    b = [0 for _ in range(N+2)]
    cnt = 1
    ans = 0
    flag = 1
    i = 0
    for i in reversed(range(N)):
        if b[a[i]+1] > 0:
            b[a[i]] = b[a[i]+1] + 1
        else:
            b[a[i]] = 1
        
    return N-max(b)
print(main())
