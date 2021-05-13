s = list(input())
t = list(input())
f = 0

for i,j in zip(s,t):
    if i==j:
        f += 1
print(f)