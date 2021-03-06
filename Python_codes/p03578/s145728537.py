from collections import Counter

n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

C = Counter(D)

for t in T:
    if C[t]:
        C[t] -= 1
    else:
        print("NO")
        exit()
print("YES")