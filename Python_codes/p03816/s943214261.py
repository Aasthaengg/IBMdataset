n = input()
A = list(map(int,input().split()))
l = len(set(A))
if(l % 2 == 0):
  l -= 1
print(l)