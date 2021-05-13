#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

inc = False
dec = False
val = 0
ans = 1
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    if inc:
        if a[i-1] > a[i]:
            ans += 1
            inc = False
    elif dec:
        if a[i-1] < a[i]:
            ans+=1
            dec =False
    else:
        if a[i-1] < a[i]:
            inc = True
        elif a[i-1] > a[i]:
            dec = True
print(ans)


