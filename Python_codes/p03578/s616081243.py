from collections import Counter
input()
D = Counter(map(int, input().split()))
input()
for n in map(int, input().split()):
    appear = D.get(n, 0)
    if not appear:
        print("NO")
        break
    D[n] -= 1
else:
    print("YES")