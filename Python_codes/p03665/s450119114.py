n, p = map(int, input().split())
a = list(map(int, input().split()))
odds = sum(i%2 for i in a)
if odds>0:
    print(2**(n-1))
elif p==0:
    print(2**(n))
else:
    print(0)