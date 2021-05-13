N = int(input())
A = list(map(int,input().split()))


odds = len([a for a in A if a % 2 == 1])

if odds % 2 == 0:
  print("YES")
else:
  print("NO")