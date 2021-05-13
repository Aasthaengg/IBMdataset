X, Y, A, B, C = map(int, input().split())
pa = list(map(int, input().split()))
pb = list(map(int, input().split()))
pc = list(map(int, input().split()))

pa = sorted(pa)
pb = sorted(pb)
pc = sorted(pc)

pr = pa[-X:] + pb[-Y:]
pr = sorted(pr)

c = 0
r = 0
while True:
  c += 1
  if c > C:
    break
  if pr[r] < pc[-c]:
    pr[r] = pc[-c]
    r += 1
  else:
    break

print(sum(pr))