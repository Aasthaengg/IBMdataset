from collections import Counter

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

ca = Counter(a)
cb = Counter(b)

for i,j in cb.items():
    if i not in ca or j > ca[i]:
        print("NO")
        exit()
print("YES")