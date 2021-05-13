n = input()
l = list(map(int, input().split()))
odd = list(filter(lambda x: (x % 2 != 0), l))
if len(odd)%2==0:
  print("YES")
else:
  print("NO")