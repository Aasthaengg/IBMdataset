N, A, B = map(int, input().split())
if (N == 1 and A != B) or A > B:
  print(0)
  exit()
min_ab = (N-1)*A+B
max_ab = (N-1)*B+A
print(max_ab-min_ab+1)