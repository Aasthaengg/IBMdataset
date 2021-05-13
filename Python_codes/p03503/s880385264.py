N = int(input())
F = [ list(map(int,input().split())) for i in range(N) ]
P = [ list(map(int,input().split())) for i in range(N) ]
ans = -float('inf')

for i in range(1, 1024):
    B = bin(i)[2::]
    count = [0]*N
    for i, b in enumerate(str(B[::-1])):
      if b == "1":
        for j, f in enumerate(F):
          if f[i] == 1:
            count[j] += 1
    l=0
    for p, c in zip(P, count):
        l += p[c]
    ans = max(ans, l)
print(ans)
