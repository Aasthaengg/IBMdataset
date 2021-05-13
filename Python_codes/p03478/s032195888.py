n,a,b = map(int, input().split())

def s(sum,a,b):
    t = 0
    if sum >= a and sum <= b:
        t = 1
    return t

def S(i):
    sum = 0
    while i > 0:
        sum += i%10
        i = int(i/10)
    return sum

num = 0
for i in range(1,n+1):
    sum = S(i)
    if s(sum,a,b) == 1:
        num += i
print(num)
