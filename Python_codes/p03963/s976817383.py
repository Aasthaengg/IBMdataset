if __name__ == "__main__":
  N, K = map(int, input().split())
  print(K*pow(K-1, N-1))