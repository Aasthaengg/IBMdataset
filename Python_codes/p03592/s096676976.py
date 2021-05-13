n, m, k = map(int,input().split())

ANS = [0] * (n*m + 1)

for i in range(n+1):
    for j in range(m+1):
        ANS[i*j + (n-i)*(m-j)] = 1
# print(ANS)
if ANS[k] == 1:
    print("Yes")
else:
    print("No")