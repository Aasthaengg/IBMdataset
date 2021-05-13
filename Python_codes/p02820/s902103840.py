N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list("x" * K + input())

win = {"r":P,"s":R,"p":S,"x":0}

ans = 0
for i in range(len(T)):
  if T[i] == T[i - K]:
    T[i] = "x"
  else:
    ans += win[T[i]]

print(ans)