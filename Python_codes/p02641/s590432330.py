import bisect

X,N = (int(x) for x in input().split())
P = list(map(int, input().split()))
ALL = list(int(i) for i in range(-100,201))
P.sort()
Q = list(set(P)^set(ALL))
number = bisect.bisect(Q,X)

if number==0:
  print(Q[0])
elif number==len(Q):
  print(Q[len(Q)-1])
elif X-Q[number-1]<=Q[number]-X:
  print(Q[number-1])
elif X-Q[number-1]>Q[number]-X:
  print(Q[number])
