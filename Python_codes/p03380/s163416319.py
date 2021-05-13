n = int(input())
a = list(map(int, input().split()))

ai = max(a)
aj = min(a)

for i in a:
    if min(aj, ai -aj) < min(i, ai - i):
        aj = i
    
print(ai, aj)