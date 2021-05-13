while True:
    N = int(input())
    if N == 0:
        break
    sum = 0
    s = input().split()
    for i in range(N):
        sum += int(s[i])
    mean = sum/N
    t = 0
    for j in range(N):
        t += (int(s[j]) - mean)**2
    b = t / N
    a = b**0.5
    print('{:.08f}'.format(a))

