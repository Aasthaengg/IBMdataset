N = int(input())
A = list(map(int, input().split()))
tmp = [i for i in A if i%2 != 0]

if (len(tmp))%2 != 1:
  print("YES")
else:
  print("NO")