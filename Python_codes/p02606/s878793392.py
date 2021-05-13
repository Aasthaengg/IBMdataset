L,R,d = map(int,input().split())
r = R//d
l = L//d
if L%d == 0:
    ans = r-l + 1
else:
    ans = r-l
print(ans)