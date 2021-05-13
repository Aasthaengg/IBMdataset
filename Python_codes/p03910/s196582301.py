N = int(input())

for x in range(N+10):
    if (x*(x+1))//2 >= N:
        break

ans = list(range(1, x+1))
rem = (x*(x+1))//2 - N
for a in ans:
    if a != rem:
        print(a)