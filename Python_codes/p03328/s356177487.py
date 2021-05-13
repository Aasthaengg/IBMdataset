ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b = nm()

s = 0

for i in range(1000):

  if b-a == i:
    print(s-a)
    break

  s+=i

