A,B,K = map(int,input().split())
if(A+B<K):
    print('0 0')
elif(A<K):
    print('0 '+str(B-(K-A)))
else:
    print(str(A-K)+' '+str(B))
