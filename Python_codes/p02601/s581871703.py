A,B,C = map(int,input().split())

K = int(input())

for x in range(K):
  if A<B*(2**x) and B*(2**x)<C*(2**(K-x)):
    print('Yes');exit()
      
print('No')