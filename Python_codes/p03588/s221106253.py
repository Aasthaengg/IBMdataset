n= int(input())
List = []
for _ in range(n):
  A, B = map(int,input().split())
  List.append([A,B])
List.sort()
Answer = List[-1][0] + List[-1][1]
print(Answer)