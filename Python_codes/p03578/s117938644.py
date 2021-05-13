from collections import defaultdict
dic = defaultdict(int) 
N = int(input())
D = list(map(int,input().split()))
for i in range(N):
  dic[D[i]] += 1


M = int(input())
T = list(map(int,input().split()))

for i in range(M):
  if dic[T[i]] == 0:
    print("NO")
    exit()
  else:
    dic[T[i]] -= 1
print("YES")