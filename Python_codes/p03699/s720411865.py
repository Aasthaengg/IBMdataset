N = int(input()) 
S = [int(input()) for i in range(N)]
S.sort()
max_ans = sum(S)

if N == 1:
  if max_ans % 10 == 0:
    print(0)
    exit(0)
  else:
    print(max_ans)
    exit(0)
if max_ans % 10 == 0:
  i = 0
  while S[i] % 10 == 0:
    i += 1
    if i == N-1:
      print(0)
      exit(0)
  ans = max_ans - S[i]
  print(ans)
else:
  print(max_ans)