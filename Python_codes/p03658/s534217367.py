N,K = map(int,input().split())

List = list(map(int,input().split()))
List = sorted(List)
for i in range(N-K):
  del List[0]

print(sum(List))