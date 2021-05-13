n,d = map(int,input().split())
D = d*2 +1
ans = 0
if n%D != 0:
    ans += 1
ans += n//D
print(ans)