n = int(input())
l = [i*j for i in range(1,10) for j in range(1,10)]
if n in l:
    print('Yes')
else:
    print('No')