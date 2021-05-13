N,M = map(int, input().split())

if min(N,M)>1:
  print(N*M-4-(N-2)*2-(M-2)*2)
elif max(N,M)==1:
  print(1)
elif min(N,M)==1:
  print(max(N,M)-2)