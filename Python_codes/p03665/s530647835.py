n, p = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in a:
    if i%2 == 0:
        count += 1
if count == n:
    if p == 1:
        print(0)
    else:
        print(2**n)
else:
    print(2**(n-1))

    
