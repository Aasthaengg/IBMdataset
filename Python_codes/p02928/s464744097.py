import collections
N,K = map(int,input().split())
A = list(map(int, input().split()))
Ni_block = 0
Ni_inter = 0
bignum = pow(10,9)+7
for i in range(N):
   for j in range(N):
      if A[i]>A[j]:
         Ni_inter += 1
         if j>i:
            Ni_block+=1
# print(Ni_inter,Ni_block)
# c = collections.Counter(A)
# N_multiple = 1
# # print(c)
# for i in c:
#    # print(i, c[i])
#    N_multiple*=c[i]
   
# print(N_multiple)
# print(len(c))
# Ndiff = len(c)
# Ni = Ni_block*K+(((K*(K-1))//2) % bignum)*(((Ni_inter*(Ni_inter-1))//2) % bignum)
Ni = Ni_block*K+(((K*(K-1))//2) % bignum)*Ni_inter
print(Ni%bignum)

