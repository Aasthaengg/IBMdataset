ans = ''
while True:
    n = int(input())
    if n == 0:
        break
    else:
        L = list(map(float, input().split(' ')))
        ave = 0
        for i in L:
            ave += i
        ave /= n
        sigma = 0
        for i in L:
            sigma += pow(i - ave, 2)
        sigma /= n
        sigma = pow(sigma, 0.5)
        ans += '{0:.8f}'.format(sigma) + '\n'
print(ans[:-1])
