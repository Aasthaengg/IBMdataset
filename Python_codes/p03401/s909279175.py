def main():
  N = int(input())
  A = [0]
  A.extend(list(map(int, input().split())))
  A.append(0)
  ans_def = 0
  for i in range(1, N+2):
    ans_def += abs(A[i]-A[i-1])
  for i in range(1, N+1):
    print(ans_def-abs(A[i-1]-A[i])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))
if __name__ == "__main__":
  main()