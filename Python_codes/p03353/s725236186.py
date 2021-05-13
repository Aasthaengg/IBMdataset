s = input()
N = len(s)
K = int(input())
ords = [ord(_s) for _s in s]
order_set = sorted(list(set(ords)))
d = set()
def add_string(o):
  for i in range(N):
    if ords[i] == o:
      for k in range(1, K+1):
        d.add(s[i:i+k])

add_string(order_set[0])
if len(d) >= K:
  print(sorted(list(d))[K-1])
  quit()

add_string(order_set[1])
if len(d) >= K:
  print(sorted(list(d))[K-1])
  quit()

add_string(order_set[2])
if len(d) >= K:
  print(sorted(list(d))[K-1])
  quit()