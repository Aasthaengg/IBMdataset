N, M, D =map(int, input().split())

if D == 0:
  P = 1/N
elif N-2*D >= 0:
  P = ((N-2*D)*2 + 2*D)/(N**2)
else:
  P = 2*(N-D)/(N**2)

print(P*(M-1))