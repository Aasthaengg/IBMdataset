n, y = map(int, input().split())
ans = [-1, -1, -1]
for senen in range(n+1):
    for gosenen in range(n-senen+1):
        itimanen = n-senen-gosenen
        if senen*1000 + gosenen*5000 + 10000*itimanen == y:
            ans = [itimanen, gosenen, senen]
            break
    else:
        continue
    break


print(*ans)