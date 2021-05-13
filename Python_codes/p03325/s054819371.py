N=int(input())
List = list(map(int, input().split()))
res = 0
flagWhile = True
flagManip = True
for i in range(N):
  while List[i] % 2 == 0:
    List[i] = List[i] //2
    res += 1

print(res)