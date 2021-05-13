n = int(raw_input())
d,x = map(int, raw_input().split())
print x + sum([1 + (d-1)/int(raw_input())  for _ in range(n)])