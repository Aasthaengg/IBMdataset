N = int(input())
A = list(map(int, input().split()))

res = float('inf')

for i in A:
    cnt = 0
    while True:
        if i % 2 == 1:
            if cnt == 0:
                print(0)
                exit()
            elif cnt < res:
                res = cnt
                break
            else:
                break
        i = i // 2
        cnt += 1

print(res)

