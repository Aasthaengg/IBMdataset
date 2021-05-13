#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())
s = [input() for _ in range(n)]

m = int(input())
t = [input() for _ in range(m)]

ss = list(set(s))
ans = [0] * len(ss)

for i in range(len(ss)):
    for j in range(n):
        if ss[i] == s[j]:
            ans[i] += 1
    for j in range(m):
        if ss[i] == t[j]:
            ans[i] -= 1

print(max(max(ans), 0))






