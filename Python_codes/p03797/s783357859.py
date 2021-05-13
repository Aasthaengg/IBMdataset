N,M = map(int,input().split())

if M < 2*N:
  answer = M//2
else:
  answer = N
  answer += (M-N*2)//4
print(answer)
