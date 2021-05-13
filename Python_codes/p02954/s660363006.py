
from math import ceil, floor

def resolve():
  S = list(input())
  N = len(S)
  result = ["0"]*N

  # print("S:", S, ", N:", N)

  start_index = 0
  while True:
    R_index = start_index
    R_length = 1
    while S[R_index+1] == "R":
      R_length += 1
      R_index += 1

    L_index = R_index+1
    end_index = L_index
    L_length = 1
    if end_index+1 <= N-1:
      while S[end_index+1] == "L":
        L_length += 1
        if end_index+1 >= N-1:
          break
        else:
          end_index += 1

    result[R_index] = str(ceil(R_length/2) + L_length//2)
    result[L_index] = str(ceil(L_length/2) + R_length//2)

    if end_index + 1 >= N - 1:
      break

    start_index = end_index + 1
  print(" ".join(result))

if __name__ == "__main__":
  resolve()