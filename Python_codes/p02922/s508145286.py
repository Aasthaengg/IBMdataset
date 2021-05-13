A, B = map(int, input().split())
if B == 1:
    print(0)
    exit()
socket = A
t = 1
while socket < B:
    t += 1
    socket = socket + A - 1
print(t)