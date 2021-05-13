def main():
  H, W, A, B = map(int, input().split())
  ans = [['0']*W for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if (i < B and j < A) or (i >= B and j >= A):
        ans[i][j] = '1'
  for i in range(H):
    print(''.join(ans[i]))
    
if __name__ == "__main__":
  main()