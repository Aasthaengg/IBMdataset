#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

s = input()

ans = "YES"
while True:
    if len(s) < 5:
        ans = "NO"
        break
    elif len(s) == 5:
        if (s != "dream" and s != "erase"):
            ans = "NO"
        break
    elif len(s) == 6:
        if (s != "eraser"):
            ans ="NO"
        break
    elif len(s) == 7:
        if (s != "dreamer"):
            ans ="NO"
        break
    else:
        if s[-5:] == "dream" or s[-5:] == "erase":
            s = s[:-5]
        elif s[-6:] == "eraser":
            s = s[:-6]
        elif s[-7:] == "dreamer":
            s = s[:-7]
        else:
            ans = "NO"
            break
print(ans)


