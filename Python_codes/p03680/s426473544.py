# coding: utf-8

N = int(input())

pushed = []
button = [0] * (N + 1)

for i in range(1, N+1):
    button[i] = int(input())

push_button = 1
for _ in range(1, N+1):
    if push_button == 2:
        print(len(pushed))
        exit(0)
    else:
        pushed.append(push_button)
        push_button = button[push_button]

print("-1")
