S = input()
A = ['R', 'U', 'D']
B = ['L', 'U', 'D']
for i,j in enumerate(S):
    if((i+1)%2==0):
        if( j not in B):
            print('No')
            exit()
    else:
        if(j not in A):
            print('No')
            exit()
print('Yes')
