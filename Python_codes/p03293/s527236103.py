#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

s = input()
t = input()


for i in range(len(s)):
    s = s[-1] + s[0:-1]
    if (s == t):
        print("Yes")
        exit()
print("No")
