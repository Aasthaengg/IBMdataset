a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
ans = 'NO'
d = abs(a-b)
m = (v-w)*t

if d-m <= 0:
    ans = 'YES'

print(ans)