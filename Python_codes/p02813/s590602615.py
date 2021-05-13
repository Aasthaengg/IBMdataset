def factorial(n):
  if n in [0, 1]:
    return 1
  else:
    return factorial(n - 1) * n

def rank_of_list(A):
  rank = 0
  for i in range(len(A)):
    rank += (A[i] - 1) * factorial(len(A) - i - 1)
    A = list(map(lambda a: a - 1 if a > A[i] else a, A))
  return rank

def main():
  N = int(input())
  P = list(map(lambda p: int(p), input().split(" ")))
  Q = list(map(lambda q: int(q), input().split(" ")))
  print(abs(rank_of_list(P) - rank_of_list(Q)))

main()