N = int(input())
lis = [list(input().split()) for i in range(N)]

new_lis = sorted(lis, key=lambda x: (x[0], -int(x[1])))

for i in new_lis:
    print(lis.index(i) + 1)