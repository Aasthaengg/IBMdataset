k,t = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

if t == 1:
    print(k-1)
else:
    m = max(a)
    print(max(m-1-(k-m), 0))