t = list(map(int, input().strip().split()))

for n in range(len(t)):
    if t[n] == 0:
        print(n+1)