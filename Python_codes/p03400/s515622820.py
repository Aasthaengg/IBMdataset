n,dd = int(raw_input()),  map(int, raw_input().split())
print dd[1] + sum([(dd[0]-1)/int(raw_input())  for _ in range(n)]) + n