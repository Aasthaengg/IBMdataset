n = int(input())
ab = []
for _ in range(n):
    ab.append(list(map(int,input().split())))

cnt = 0
for i in range(n-1,-1,-1):
    a,b = ab[i][0],ab[i][1]
    num = a + cnt
    if num % b == 0:
        continue
    else:
        amari = num % b
        cnt += b-amari
    
print(cnt)