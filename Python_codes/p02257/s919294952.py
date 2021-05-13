def IsPrime(n):
    '''

    :param n:??£??´??°
    :return: ?´???°?????????True, ????????????????????°?????????False
    ???????????§???????´???°??? 6k-1????????? 6k+1??§??¨?????????????????????k?????£??´??°
    '''
    if n == 2 or n == 3 or n== 5: return True
    if n == 1 or n%2 == 0 or n%3 == 0:return False
    d, l = 5, int(n**(1/2))
    while d <= l:
        if n%d == 0 or n%(d+2) == 0:return False
        d += 6
    return True
c = 0
for i in range(int(input())):
    if IsPrime(int(input())): c += 1
print(c)