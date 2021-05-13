n = int(input())

count = [0]*(n+1)
P = map(int, (input() for _ in range(n)))
for p in P:
    count[p]=count[p-1]+1    

print(n - max(count))