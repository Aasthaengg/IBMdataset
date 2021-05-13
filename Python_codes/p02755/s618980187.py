import math
A, B = map(int, input().split())
candidate_a = []
candidate_b = []

def candidate(tax, tax_rate, candidate):
  candidate.append(math.ceil(tax / tax_rate))
  i = candidate[0] + 1
  while tax == math.floor(i * tax_rate):
    candidate.append(i)
    i += 1

candidate(A, 0.08, candidate_a)
candidate(B, 0.1, candidate_b)

if candidate_a[0] <= candidate_b[0]:
  if candidate_a[-1] >= candidate_b[0]:
    print(candidate_b[0])
  else: 
    print(-1)
else:
  if candidate_b[-1] >= candidate_a[0]:
    print(candidate_a[0])
  else:
    print(-1) 