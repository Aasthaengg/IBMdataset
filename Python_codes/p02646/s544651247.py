a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
ans = "NO"
if v>w and abs(a-b)/(v-w)<=t:
    ans = "YES"
print(ans)