n = input()
l = list(map(int,input().split()))
cnt = 0

while True:
    if len([i for i in l if i%2 == 1]) == 0:
        cnt += 1
        l = [int(s/2) for s in l]
    else:
        break

print(cnt)