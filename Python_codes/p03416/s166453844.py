a,b = map(int,input().split())
cnt = 0
def palin(x):
    global cnt
    s = str(x)
    if s[0]==s[4] and s[1]==s[3]:
        cnt += 1
    return cnt
for i in range(a,b+1):
    palin(i)
print(cnt)