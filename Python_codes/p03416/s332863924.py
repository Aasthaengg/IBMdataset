n,m = map(int,input().split())

def judge (x):
    if x[0] == x[4] and x[1] == x[3]:
        return True
    else:
        return False

ans = 0
for i in range(n,m+1):
    if judge(str(i)):
        ans += 1

print (ans)
