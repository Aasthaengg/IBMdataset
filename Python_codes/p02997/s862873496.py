def main():
  N, K  = map(int, input().split())
  max_pair = (N-1)*(N-2)//2
  if max_pair < K:
    print(-1)
  else:
    edge = []
    for i in range(N-1):
      edge.append([1, 2+i])
    from_ = 2
    to_ = 3
    for i in range(max_pair-K):
      edge.append([from_, to_])
      to_ += 1
      if to_ > N:
        from_ += 1
        to_ = from_ + 1
    num = len(edge)
    print(num)
    [print(*edge[i]) for i in range(num)]
    
if __name__ == "__main__":
  main()  