N, X, T = map(int,input().split())
counter = 0
rem = N
while rem > 0:
    rem -= X
    counter += 1
print(counter*T)
