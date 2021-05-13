N,M = map(int,input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
for dx in range(N-M+1):
    for dy in range(N-M+1):
        flg = True
        for i in range(M):
          if A[i+dx][dy:dy+M] != B[i]:
            flg = False
            break
        if flg:
          print("Yes")
          exit()
print("No")
