N, K = list(map(int,input().split()))
S = input()
ls = list(S)
if ls[K-1] == 'A':
  ls[K-1] = 'a'
elif ls[K-1] == 'B':
  ls[K-1] = 'b'
elif ls[K-1] == 'C':
  ls[K-1] = 'c'
print(''.join(ls))