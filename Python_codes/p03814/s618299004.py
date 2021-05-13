#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

s = input()

a = 500000000000
z = -1

for i in range(len(s)):
    if s[i] == "A":
        a = min(a,i)
    elif s[i] == "Z":
        z = max(z,i)
print(z-a+1)
