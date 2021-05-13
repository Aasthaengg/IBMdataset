#coding:utf-8
n = int(input())
#これだけでも二次元リストができる
st = [input().split() for _ in range(n)]
x = input()
flag = False
ans = 0
#print(st)

for s, t in st:
    if flag == True:
        ans += int(t)
    if s == x:
        flag = True

print(ans)