n = int(input())
abc = [input() for i in range(3)]
d = [0]*n
for i in range(n):
    if abc[0][i]==abc[1][i]==abc[2][i]:
        d[i]=0
    elif abc[0][i]!=abc[1][i]!=abc[2][i]!=abc[0][i]:
        d[i]=2
    else:
        d[i]=1
print(sum(d))