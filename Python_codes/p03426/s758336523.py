def main():
  H, W, D = map(int, input().split())
  num = [[] for _  in range(H*W)]
  for i in range(H):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
      num[temp[j]-1] = [i, j]
  #num = np.array(num)
  num_sum = [0]*(H*W)
  for i in range(D, H*W):
    num_sum[i] = num_sum[i-D] + (abs(num[i][0]-num[i-D][0])+ abs(num[i][1]-num[i-D][1]))
  Q = int(input())
  ans = []
  for i in range(Q):
    L, R = map(int, input().split())
    ans.append(num_sum[R-1]-num_sum[L-1])
  print(*ans, sep='\n')
if __name__ == "__main__":
  main()