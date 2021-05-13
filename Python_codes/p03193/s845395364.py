N,H,W = (int(i) for i in input().split())

count = 0
for i in range(N):
    A,B = (int(k) for k in input().split())
    if A>=H and B>=W:
        count += 1

print(count)