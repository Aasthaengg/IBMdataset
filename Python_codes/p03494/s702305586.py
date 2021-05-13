_ = input()
a = [int(i) for i in input().split()]

cnt = 0
while all(not i % 2 for i in a):
    a = [i // 2 for i in a]
    cnt += 1
else:
    print(cnt)