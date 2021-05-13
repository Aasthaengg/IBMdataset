N = int(input())
A = map(int,input().split())
n_odd = [odd for odd in A if odd%2==1]
if len(n_odd)%2==1:
  print("NO")
else:
  print("YES")