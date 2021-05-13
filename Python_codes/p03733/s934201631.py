N,T = map(int,input().split())
t = list(map(int,input().split()))
ma = t[-1] + T
mainasu = 0

for i in range(N-1):
    if t[i+1] - t[i] <T:
        continue
    else:
         mainasu += t[i+1] - t[i] - T
print(ma - mainasu)