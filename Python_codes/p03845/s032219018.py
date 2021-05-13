n = int(input())
t = [int(i) for i in input().split()]
s = sum(t)
m = int(input())
ans = []
for _ in range(m):
    p,x = map(int,input().split())
    p -= 1
    ans.append(s-t[p]+x)
print("\n".join(map(str,ans)))