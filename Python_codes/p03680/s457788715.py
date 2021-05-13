def resolve():
  N = int(input())
  A = [0]*(N+1)

  for i in range(N):
    A[i+1] = int(input())

  move_count = 0
  next_index = 1
  for _ in range(N):
    move_count += 1
    if A[next_index] == 2:
      print(move_count)
      return True
    elif A[next_index] == 0:
      print(-1)
      return True
    else:
      temp = next_index
      next_index = A[temp]
      A[temp] = 0

if __name__ == "__main__":
  resolve()