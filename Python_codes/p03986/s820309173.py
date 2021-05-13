X = input()

left_S = 0
left_T = 0

for i in range(len(X)):
    if X[i] == "S":
        left_S += 1
    elif left_S == 0:
        left_T += 1
    else:
        left_S -= 1

print(left_S + left_T)