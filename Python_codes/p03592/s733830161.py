def resolve():
    n, m, k = map(int, input().split())
    OK = False
    for i in range(n+1):
        for j in range(m+1):
            if i*m+(n-2*i)*j == k:
                OK = True
    if OK:
        print("Yes")
    else:
        print("No")
resolve()