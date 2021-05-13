n = int(input())
print(0, flush=True)
syo = 0
s = input()
if s == "Vacant":
  exit()
syos = s
dai = n-1
print(n-1, flush=True)
s = input()
dais = s
if s == "Vacant":
  exit()
for _ in range(18):
  mid = (dai+syo)//2
  print(mid, flush=True)
  s = input()
  if s == "Vacant":
    exit()
  if ((mid - syo)%2 == 0 and s != syos) or ((mid - syo)%2 == 1 and s == syos):
    dai = mid
    dais = s
  else:
    syo = mid
    syos = s