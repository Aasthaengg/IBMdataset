# from math import ceil
def ceil(x,y):
  return (x-1)//y+1
N = int(input())
TA = [list(map(int, input().split())) for _ in range(N)]
t, a = 1, 1
for T, A in TA:
  rate = max(ceil(t, T), ceil(a, A))
  t = T * rate
  a = A * rate
print(t + a)    
    
