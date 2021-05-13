A, B = map(int, input().split())

socket = 1
cnt_A = 0
while socket < B:
    socket += A-1
    cnt_A += 1

print(cnt_A)