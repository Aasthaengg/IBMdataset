k, t = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

ma = a[0]
ex = sum(a[1:])
diff =  ma - ex
if diff > 0:
    print(diff - 1)
else:
    print(0)
