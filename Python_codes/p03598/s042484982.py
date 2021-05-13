N = int(input())
K = int(input())
List = list(map(int,input().split()))
ans = 0
for i in range(N):
  x = List[i]
  ans = ans + min(abs(0-x),abs(K-x))*2
print(str(ans))