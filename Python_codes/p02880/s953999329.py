N=int(input())
A=[]
for i in range(1,10):
    for j  in range(1,10):
        if i*j==N:
            A.append('Yes')
        else:
            A.append('No')
if 'Yes' in A:
    print('Yes')
else:
    print('No')