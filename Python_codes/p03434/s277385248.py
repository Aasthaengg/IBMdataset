N = int(input())
List = list(map(int, input().split()))
List.sort(reverse=True)
A = 0
B = 0
for i in range(N):
  if i % 2 ==0:
    A += List.pop(0)
  else:
    B += List.pop(0)
print(A-B)