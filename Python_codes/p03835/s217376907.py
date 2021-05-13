K,S=[ int(r) for r in input().split(' ') if r != '' ]
max_range=min(K,S)
cnt=0
for x in range(max_range+1):
    for y in range(min(max_range,max(0,S-x-max_range)),min(max_range,S-x)+1):
        z= S-x-y
        if 0 > z:
            break
        if z <= max_range:
            cnt+=1
print(cnt)
