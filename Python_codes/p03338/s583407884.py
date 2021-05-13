#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())
s = input()

ans = 0
for i in range(n-1):
    cnt = 0
    f = set(s[:i+1])
    b = set(s[i+1:])
    tmp = []
    if (len(f) >= len(b)):
        tmp = list(set(s[:i+1]))
        tmp2 = list(s[i+1:])
    else:
        tmp = list(set(s[i+1:]))
        tmp2 = list(s[:i+1])
    for i in range(len(tmp)):
        if tmp[i] in tmp2:
            cnt += 1
    ans = max(ans, cnt)
print(ans)




