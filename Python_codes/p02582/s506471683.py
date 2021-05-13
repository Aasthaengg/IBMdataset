S = str(input())
count = 0
if S == "RSR":
    print(1)
else:
    for i in range(0, 3):
        if S[i] == "R":
            count += 1
    print(count)