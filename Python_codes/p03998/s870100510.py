#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a = input()
b = input()
c = input()

temp = a[0]
a = a[1:]

ans = "A"
while True:
    if temp == "a":
        if len(a) == 0:
            ans = "A"
            break
        else:
            temp = a[0]
            a = a[1:]
    elif temp == "b":
        if len(b) == 0:
            ans = "B"
            break
        else:
            temp = b[0]
            b = b[1:]
    else:
        if len(c) == 0:
            ans = "C"
            break
        else:
            temp = c[0]
            c = c[1:]

print(ans)

