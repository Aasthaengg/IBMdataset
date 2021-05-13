n = int(input())
song = []
if n == 1:
    print(0)
else:
    for i in range(n):
        title, time = input().split()
        song.append([title, int(time)])

    check = input()
    flag = False
    ans = 0
    for k, v in song:
        if k == check:
            flag = True
            continue
        if flag:
            ans += v
    print(ans)
