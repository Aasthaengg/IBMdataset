N = int(input())
A = list(map(int,input().split()))
t = 0
for e in A:
    t += e%2
print("YES" if t%2 == 0 else "NO")
