D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]

def calc(D, s, t):
  last = [0 for _ in range(26)]
 
  value = 0
  for i in range(D):
    day = i + 1
    value += s[i][t[i]-1]
    last[t[i]-1] = day
    for j in range(26):
      value -= c[j] * (day - last[j])
    print(value)
calc(D, s, t)