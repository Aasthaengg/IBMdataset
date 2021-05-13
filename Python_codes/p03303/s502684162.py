S = input()
w = int(input())

for i, si in enumerate(S):
    if i % w == 0:
        print(si, end='')