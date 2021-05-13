#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a,b,c,d = map(int, input().split())

ans = "Yes"
if abs(a-c) <= d:
    pass
elif abs(a-b) <= d and abs(b-c) <= d:
    pass
else:
    ans = "No"
print(ans)


