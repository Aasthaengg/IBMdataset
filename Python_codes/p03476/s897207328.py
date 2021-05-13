import math

n = int(input())
a = 0
li = [] #累積和のリスト
ans = []

def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

for i in range(10**5//2):
    x = 2*i+1
    y = i+1
    if is_prime(y):
        if is_prime(x):
            a += 1
    li.append(a)

for i in range(n):
    l, r = map(int,input().split())
    ans.append(li[r//2]-li[max(0,l//2-1)])

for i in ans:
    print(i)