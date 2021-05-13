N = int(input())
A = input()
B = input()
C = input()

l = [[a, b, c] for a, b, c in zip(A, B, C)]

cnt = 0
for i in range(N):
    l_set = set(l[i])
    if len(l_set) == 1:
        pass
    elif len(l_set) == 2:
        cnt += 1
    else:
        cnt += 2

print(cnt)