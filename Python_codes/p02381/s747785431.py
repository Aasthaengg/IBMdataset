while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    m = sum(s)/n
    a2 = sum([(s[i] - m)**2 for i in range(n)])/n
    a = a2**0.5
    print(a)