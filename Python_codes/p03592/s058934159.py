H,W,target = map(int,input().split())
res = 'No'
for w in range(0,W+1):
    for h in range(0,H+1):
        num_black = w * h + (W-w)*(H-h)
        if num_black == target:
            res = 'Yes'
print(res)