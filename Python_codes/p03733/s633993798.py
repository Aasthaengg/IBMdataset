N, T = map(int,input().split())
t = list(map(int,input().split()))
s = 0
start = 0
end = 0
for p in t:
  if end > p:
    end = p+T
  else:
    s += (end - start)
    start = p
    end = p+T
s += end - start
print(s)