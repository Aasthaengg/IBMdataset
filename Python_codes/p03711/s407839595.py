A = [1,3,5,7,8,10,12]
B = [4,6,9,11]

a,b = [int(i) for i in input().split()]

if a in A and b in A:
    print('Yes')
elif a in B and b in B:
    print('Yes')
else:
    print('No')
