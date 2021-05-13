n=int(input())
s=input()

sumBlack = [0]*(n+1)
sumWhite = [0]*(n+1)
for i in range(1,n+1):
    sumBlack[i] = sumBlack[i-1]
    if s[i-1] == '#':
        sumBlack[i] += 1

for i in range(n-1,-1,-1):
    sumWhite[i] = sumWhite[i+1]
    if s[i] == '.':
        sumWhite[i] += 1

ans = 12345678901234
for i in range(n+1):
    ans = min(ans,sumBlack[i]+sumWhite[i])
print(ans)