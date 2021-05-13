flag = False
mini = 124
time = 0
for _ in range(5):
    A = int(input())
    if A%10 == 0:
        time += A
    else:
        time += A - A%10 + 10
        mini = min(A%10, mini)
        flag = True
if flag:
    time += mini - 10
print(time)