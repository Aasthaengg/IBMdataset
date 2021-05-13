K,S=[ int(r) for r in input().split(' ') if r != '' ]
max_loop=min(K,S)+1
cnt=0
for x in range(max_loop):
    for y in range(max_loop):
        z= S-x-y
        if 0 > z:
            break
        if z <= K:
            cnt+=1
print(cnt)
