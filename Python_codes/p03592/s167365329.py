N,M,K = map(int,input().split())
ans = "No"

for a in range(N+1):
  if N - 2*a != 0:
    if (K - a*M) % (N - 2*a) == 0:
      if M >= (K - a*M) / (N - 2*a) >= 0:
        ans = "Yes"
print(ans)