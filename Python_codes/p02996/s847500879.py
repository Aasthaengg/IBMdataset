N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
# Bについてソート
AB = sorted(AB, key=lambda x: x[1])
time = 0
for job in AB:
    # Aを足す
    time += job[0]
    # 期限を過ぎてしまった場合
    if time > job[1]:
        print("No")
        exit()
print("Yes")
