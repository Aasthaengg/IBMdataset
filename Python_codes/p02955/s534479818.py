N, K  = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
#print(S)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

S_div = make_divisors(S)

mod = []
for _ in range(N):
  mod.append(0)

ans = 1
for i in range(1,len(S_div)):
  for j in range(N):
    mod[j] = A[j] % S_div[i]
  group = sum(mod)//S_div[i]
  mod.sort(reverse=True)
  Ktmp = S_div[i]*group - sum(mod[:group])
  if Ktmp <= K:
    ans = max(ans,S_div[i])

print(ans)