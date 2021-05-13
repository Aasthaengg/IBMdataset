l = input().split(' ')

l = list(map(int, l))

if l[2] >= l[0] and l[2] <= l[1]:
    print ('Yes')
else:
    print ('No')