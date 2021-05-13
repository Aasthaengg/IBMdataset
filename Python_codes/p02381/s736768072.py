while True:
    n = int(input())
    if n==0:
        break
    s = list(map(float, input().split()))
    m = sum(s) / n
    var = sum([(s[i] - m)**2 for i in range(n)]) / n
    print("{:.5f}".format(var**0.5))