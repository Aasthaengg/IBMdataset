
def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  if N == 0 and A[0] != 1:
    print(-1)
    return True
  min_maxs = [0] * len(A)
  min_maxs[len(A)-1] = [A[-1], A[-1]]

  for index in reversed(range(len(A)-1)):
    min_maxs[index] = [min_maxs[index+1][0] // 2 + A[index], min_maxs[index+1][1] + A[index]]

  result = 1
  recent = 1
  for index in range(1, len(A)):
    num_of_node = (recent - A[index-1]) * 2
    if num_of_node < min_maxs[index][0]:
      print(-1)
      return True
    
    result += min(num_of_node, min_maxs[index][1])
    recent = min(num_of_node, min_maxs[index][1])

  print(result)

if __name__ == "__main__":
    resolve()