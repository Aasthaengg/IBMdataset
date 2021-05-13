n = int(input())
a = list(map(int,input().split()))

a_1 = int(len(a))
a_2 = int(len(set(a)))
if a_1 == a_2:
  print("YES")
else:
  print("NO")