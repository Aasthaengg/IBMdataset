N = int(input())
bL = [int(input()) for _ in range(N)]

time = 0
push = 0
while True:
    time += 1
    if bL[push] == 2:
        print(time)
        break
    if time == N:
        print("-1")
        break
    push = bL[push]-1