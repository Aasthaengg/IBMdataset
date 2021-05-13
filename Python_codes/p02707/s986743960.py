N = int(input())
p = list(map(int, input().split()))
sya = [0]*N
t = 0



for i in range(N-1):
  t = p[i-1]
  sya[t-1] +=1



print('\n'.join(map(str, sya)))