K = int(input())
if K%2 == 1:
  odd = K//2+1
  even = K//2
else:
  odd = K//2
  even = K//2
print(odd*even)