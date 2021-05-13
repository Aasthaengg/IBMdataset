from collections import Counter
N = map(int, input().split())
A = list(map(int, input().split()))
dic=Counter(A)
for val in dic.values():
    if val > 1:
        print("NO")
        exit()

print("YES")