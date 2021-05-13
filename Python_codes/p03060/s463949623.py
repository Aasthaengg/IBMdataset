N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

value = 0
for i in range(len(V)):
    if V[i]-C[i]>0:
        value += (V[i]-C[i])
    else:
        continue

print(value)