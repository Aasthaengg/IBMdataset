n = int(input())
abc = []
for _ in range(3):
    abc.append(str(input()))
cnt = 0
for i in range(n):
    if abc[0][i]==abc[1][i]==abc[2][i]:
        cnt += 0
    elif (abc[0][i]==abc[1][i]!=abc[2][i])\
        or (abc[1][i]==abc[2][i]!=abc[0][i])\
        or (abc[2][i]==abc[0][i]!=abc[1][i]):
        cnt += 1
    else:
        cnt += 2
print(cnt)