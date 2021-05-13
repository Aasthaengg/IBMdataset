n = int(input())
bs = list(map(int, input().split()))
sb = [0] * n
for i in bs:
    sb[i - 1] += 1
for i in sb:
    print(i)