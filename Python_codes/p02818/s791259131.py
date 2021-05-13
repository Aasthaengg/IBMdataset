a, b, k = [int(i) for i in input().split()]
aa = a - k if a - k > 0 else 0
k =  k - a if k - a > 0 else 0
bb = b - k if b - k > 0 else 0
print(str(aa) + ' ' + str(bb))