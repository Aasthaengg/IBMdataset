a, b, k = [int(i) for i in input().split()]

if k < b-a+1:
    tmp1 = list(range(a, a+k))
    tmp2 = list(range(b-k+1, b+1))
    tmp1.extend(tmp2)
    tmp = sorted(list(set(tmp1)))
    
else:
    tmp = list(range(a, b+1))
    
for i in tmp:
    print(i)
