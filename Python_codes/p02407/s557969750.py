N = int(input())

i = list(map(int, input().split()))
i.reverse()

for idx, val in enumerate(i):
    if idx == N-1:
        print(val)
    else:
        print(val, ' ', sep = '', end='')
