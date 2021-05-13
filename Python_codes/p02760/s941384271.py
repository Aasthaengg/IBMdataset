Aij= [input().split() for l in range(3)]
N=int(input())
b= [int(input()) for i in range(N)]
for j in range(3):
    for k in range(3):
        for n in range(N):
            if int(Aij[j][k])==b[n]:
                Aij[j][k]='0'
if Aij[0].count('0')==3 or Aij[1].count('0')==3 or Aij[2].count('0')==3:
    print('Yes')
elif Aij[0][0]=='0' and Aij[1][0]=='0' and Aij[2][0]=='0':
    print('Yes')
elif Aij[0][1]=='0' and Aij[1][1]=='0' and Aij[2][1]=='0':
    print('Yes')
elif Aij[0][2]=='0' and Aij[1][2]=='0' and Aij[2][2]=='0':
    print('Yes')
elif Aij[0][0]=='0'and Aij[1][1]=='0'and Aij[2][2]=='0':
    print('Yes')
elif Aij[0][2]=='0' and Aij[1][1]=='0'and Aij[2][0]=='0':
    print('Yes')
else:
    print('No')