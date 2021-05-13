MOD=10**9+7
N,K=map(int,input().split())

inv_table = [0]+[1]
for i in range(2,K+2):
  inv_table.append(-(MOD//i)*inv_table[MOD%i]%MOD)
  
term1=N-K+1
term2=1
for i in range(1,K+1):  
  #print(term1,term2)  
  print((term1*term2)%MOD)

  term1=term1*(N-K+1-i)*inv_table[i+1]%MOD
  term2=term2*(K-i)*inv_table[i]%MOD