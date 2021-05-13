n = int(input())
s = input()
countwhite = [0] * (n+1)
countblack = [0] * (n+1)

#whitecount
cnt = 0
for i in range(n):
    if s[i] == "#":
        cnt += 1
    countwhite[i+1] = cnt

cnt = 0
for i in range(n-1, -1, -1):
    if s[i] == ".":
        cnt += 1
    countblack[i] = cnt

#print(countwhite)
#print(countblack)
res = 999999999999999
for i in range(n+1):
    res = min(res, countblack[i] + countwhite[i])
print(res)