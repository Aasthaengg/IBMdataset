N = int(input())
X_2 = input()
X_10 = int(X_2, 2)

y = X_2.count('1')

a = X_10%(y+1)
if y==1:
    b = 0
else:
    b = X_10%(y-1)

for i in range(N):
    if X_2[i] == '1' and y == 1:
        print(0)
        continue
    elif X_2[i] == '1':
        x = (b-pow(2, N-1-i, y-1))%(y-1)
    else:
        x = (a+pow(2, N-1-i, y+1))%(y+1)
    count = 1
    while x!=0:
        x %= bin(x)[2:].count('1')
        count += 1
    print(count)