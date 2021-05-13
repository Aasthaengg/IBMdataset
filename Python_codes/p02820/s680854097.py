#abc149_d
from sys import stdin

#stdin = open("test/abc149_d_sample-2.in")

N, K = map(int, stdin.readline().strip().split(" "))
R, S, P = map(int, stdin.readline().strip().split(" "))
T = stdin.readline().strip()

pmap = {
  "r": R,
  "s": S,
  "p": P
}

winmap = {
  "r": "p",
  "s": "r",
  "p": "s"
}

point = 0
T2 = list(T)
#print(N,K)

for i,t in enumerate(T):
  #print(t)
  wintp = "x"
  if i>K-1:
    tp = T2[i-K]
    if tp!="x":
      wintp = winmap[tp]
  
  wint = winmap[t]
  if wint!=wintp:
    point += pmap[wint]
  else:
    T2[i] = "x"

#print(T2)
print(point)
