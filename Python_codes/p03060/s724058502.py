n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

r = []
for i, j in zip(v,c):
    if i>j:
        r.append(i-j)
print(sum(r))