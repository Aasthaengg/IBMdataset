N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ansl = []

for i in range(N):
    total = sum(A1[0:i+1]) + sum(A2[i:])
    ansl.append(total)

print(max(ansl))