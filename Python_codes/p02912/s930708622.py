import sys
input=sys.stdin.readline

N,M = (int(x) for x in input().rstrip('\n').split())
As = [int(x) for x in input().rstrip('\n').split()]
As = sorted(As,reverse = True)
rest = M
for _ in range(M):
  if rest == 0:
    break
  d = As[0]
  b = d//2 - d//4
  for i in range(N):
    a = As[i]
    check = 0
    if a-a//2<b:
      if rest > i:
        ad = [x//2 for x in As[:i]]
        As = As[i:]
        As.extend(ad)
        rest -= i
        check += 1
        As = sorted(As,reverse = True)
        break
      else:
        ad = [x//2 for x in As[:rest]]
        As = As[rest:]
        As.extend(ad)
        check += 1
        rest = 0
        break
    if i == N-1:
      if check == 0:
        if rest > N:
          As = [x//2 for x in As]
          rest -= N
        else:
          ad = [x//2 for x in As[:rest]]
          As = As[rest:]
          As.extend(ad)
          rest = 0
          break
print(sum(As))
