n = int(input())
la = [int(w) for w in input().split()]

x = la[0]

for a in la[1:]:
    x ^= a

cond = x == 0
print("Yes" if cond else "No")
