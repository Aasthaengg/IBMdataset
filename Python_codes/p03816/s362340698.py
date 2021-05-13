n = int(input())
a = list(map(int, input().split()))

a_set_len = len(set(a))
if (len(a)-a_set_len) % 2 == 0:
  print(a_set_len)
else:
  print(a_set_len-1)