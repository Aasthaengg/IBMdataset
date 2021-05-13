#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a,b,c = map(int, input().split())

ans = "No"

if a + b == c or a + c == b or b + c == a:
    ans = "Yes"

print(ans)
