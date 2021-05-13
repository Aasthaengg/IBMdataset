import math
while True:
    n = int(input())
    if n == 0:
        break
    a = 0
    st = list(map(int, input().split()))
    m = sum(st)/len(st)
    for x in st:
        a += (x-m)**2
    print(math.sqrt(a/n))
    

