ll = list(map(int, input().split()))
ll.sort()

cnt = ll[2] + ll[2] - ll[1] - ll[0]

if cnt%2 == 0:
    print(cnt//2)
else:
    cnt -= 3
    print(cnt//2+3) 