K, A, B = map(int,input().split())

if B - A <= 2 or K < A + 1:
  print(K+1)
else:
  cnt = A - 1
  bisket = 1 + cnt + (B - A) * ((K - cnt)//2)
  bisket += (K - cnt) % 2
  print(bisket)