W,B=map(int,input().split())
U,D=['#']*1000,['.']*1000
for i in range(W-1):U[i*2]='.'
for i in range(B-1):D[i*2]='#'
print(80,50)
for x in range(20):print(''.join(U[x*50:-~x*50])+'\n'+'#'*50)
for x in range(20):print('.'*50+'\n'+''.join(D[x*50:-~x*50]))