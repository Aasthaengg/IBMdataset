a,b=map(int, input().split())
c=sorted(list(map(int, input().split())),reverse = True)

ans = 0

if b >= a:
    c = [0]
if b < a:
    for i in range(b):
        c[i] = 0

print(sum(c))
