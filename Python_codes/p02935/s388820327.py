N=int(input())
List = list(map(int, input().split()))
List.sort()
for i in range(N-1):
  res = (List.pop(0)+List.pop(0))/2
  List.append(res)
  List.sort()
print(res)