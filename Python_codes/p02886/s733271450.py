N = int(input())
D = tuple(map(int, input().split()))
s = 0
for i in range(0, len(D)-1):
    for j in range(i+1, len(D)):
        s += D[i] * D[j]
print(s)
