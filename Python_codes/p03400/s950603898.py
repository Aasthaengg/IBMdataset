n = int(input())
d,x = map(int,input().split())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)

ans = 0
for i in l:
    tmp = (d-1)//i
    ans += tmp+1

print(ans+x)