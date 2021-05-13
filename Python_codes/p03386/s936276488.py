a,b,k = list(map(int,input().split()))

a_l = [a+i for i in range(k)]
b_l = [b-i for i in range(k)]
if b-a < k:
    [print(i) for i in range(a,b+1)]
else:
    [print(i) for i in sorted(set(a_l+b_l))]
