N = int(input())
flag = True
for _ in range(N):
    flag &= (int(input()) % 2 == 0)

print('second' if flag else 'first')