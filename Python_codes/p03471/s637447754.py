N, Y = map(int, input().split())

c =False
for i in range(N+1):
    for j in range(N+1-i):
        if Y == 10000*i + 5000*j + 1000*(N-i-j):
            a = [str(i), str(j), str(N-i-j)]
            print(" ".join(a))
            c = True
            break
    if c:
        break
if not c:
    print("-1 -1 -1")
