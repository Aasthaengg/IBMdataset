import math
def check(n,a):
    l1 = []
    l2 = []
    count1 = 0
    count2 = 0
    for i in range(len(a)):
        if a[i]%n > n - a[i]%n:
            count1 = count1 + n - a[i]%n
            l1.append(n-a[i]%n)
        else:
            count2 = count2 + a[i]%n
            l2.append(a[i]%n)
    b = (count2 - count1) // n
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    if b == 0:
        return count1
    elif b > 0:
        for i in range(b):
            count2 = count2 - l2[i]
        return count2
    else:
        for i in range(-1*b):
            count1 = count1 - l1[i]
        return count1
n,k = map(int,input().split())
a = list(map(int,input().split()))
p = sum(a)
l = []
for i in range(1,int(math.sqrt(p))+1):
    if p%i == 0:
        l.append(i)
        if i != p//i:
            l.append(p//i)
l.sort(reverse=True)
for i in range(len(l)):
    if check(l[i],a) <= k:
        print(l[i])
        break