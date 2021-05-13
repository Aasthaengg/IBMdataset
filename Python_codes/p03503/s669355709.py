N = int(input())
Fs = []
for _ in range(N):
    Fs.append(list(map(int, input().split())))

Ps = []
for _ in range(N):
    Ps.append(list(map(int, input().split())))


def calc(isOpen):
    global ans
    isAllClose = True
    for i in range(10):
        if isOpen[i]:
            isAllClose = False

    if isAllClose:
        return

    rieki = 0
    for i in range(N):
        count = 0
        for j in range(10):
            if Fs[i][j] and isOpen[j]:
                count += 1

        rieki += Ps[i][count]

    ans = max(ans, rieki)


def search(isOpen):
    if len(isOpen) == 10:
        calc(isOpen)
    else:
        search(isOpen + [True])
        search(isOpen + [False])


ans = -float('inf')
search([])

print(ans)
