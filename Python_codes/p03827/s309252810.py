N = int(input())
S = input()
X = [0]
x = 0

for i in S:
    if i == 'I':
        x += 1
        X += [x]
    else:
        x -= 1
        X += [x]
print(max(X))