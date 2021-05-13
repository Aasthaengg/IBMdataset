
n=int(input())
if n%1000==0:
    print('0')
else:
    k = n
    k += 1000
    k //= 1000
    cha = k*1000-n
    print(cha)