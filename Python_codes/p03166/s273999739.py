N, M = map(int,raw_input().split())
gra = [set() for n in range(N)]
ins = [0] * N

start = set(range(N))
for m in range(M) :
  x, y = map(int,raw_input().split())
  gra[x-1].add(y-1)
  ins[y-1] += 1
  start.discard(y-1)

mem = [None for n in range(N)]
q = list(start)
for i in q : mem[i] = 0

longest = 0
while q :
  cur = q.pop(0)
  for nxt in gra[cur] :
    ins[nxt] -= 1
    if ins[nxt] == 0 :
      mem[nxt] = mem[cur] + 1
      longest = max(longest, mem[nxt])
      q.append(nxt)

print longest