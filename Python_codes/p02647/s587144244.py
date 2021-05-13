def action(A, N):
  B = [0] * N
  for i, bright in enumerate(A):
    s = max(0, i - bright)
    B[s] += 1
    e = min(N, i + bright)
    if e < N - 1:
      B[e + 1] -= 1
  
  for i in range(N - 1):
    B[i + 1] += B[i]
  return B

def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))

  for i in range(K):
    A = action(A, N)
    if (A[0] == N) & all(A):
      break
      
  print(*A, sep=" ")

if __name__ == '__main__':
  main()