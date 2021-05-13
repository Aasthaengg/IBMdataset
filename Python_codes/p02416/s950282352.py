X = []
while(True):
    x = input()
    if x =="0":
        break
    else:
        X.append(x)
for i in range(len(X)):
    x_sum = 0
    for j in X[i]:
        x_sum += int(j)
    print(x_sum)
