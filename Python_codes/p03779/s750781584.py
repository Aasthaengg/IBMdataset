# ABC 056 C
X =int(input())
for t in range(10**9):
    if t * (t+1)/2 >=X:
        print(t)
        exit()