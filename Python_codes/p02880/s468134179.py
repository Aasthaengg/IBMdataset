N = int(input())

ANS = 'No'
for a in range(1, 10):
    for b in range(1, 10):
        if a * b == N:
            ANS = 'Yes'
            break
    if ANS == 'Yes':
        break
print(ANS)