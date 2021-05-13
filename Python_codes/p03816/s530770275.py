N = int(input())
List = list(map(int,input().split()))
sorts =len(set(List))
if (N - sorts)%2 ==0:
  print(sorts)
else:
  print(sorts - 1)