N,H,W = list(map(int,input().split()))
ABL = [list(map(int,input().split())) for _ in range(N)]
count = 0
for AB in ABL:
    if AB[0] >= H and AB[1] >= W:
        count += 1
print(count)