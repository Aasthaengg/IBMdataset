N = int(input())
d_list = list(map(int, input().split()))
d_list = sorted(d_list)

if N % 2 != 0:
  print(0)
else:
  middle = N // 2 
  answer = d_list[middle] - d_list[middle - 1]
  print(answer)