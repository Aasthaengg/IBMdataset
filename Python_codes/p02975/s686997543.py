from collections import Counter
N = int(input())
A = list(map(int, input().split()))
SA = set(A)
CA = Counter(A)

if len(SA) == 1 and list(SA)[0] == 0:
    print("Yes")
    exit()

if len(SA) == 2 and 0 in SA and CA[0] * 3 == N:
    print("Yes")
    exit()

for v in CA.values():
    if 3 * v != N:
        break
else:
    a, b, c = CA.keys()
    if a ^ b ^ c == 0:
        print("Yes")
        exit()

print("No")