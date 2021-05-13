o = list(input())
e = list(input())
ans = ''
for i in range(len(e)):
    ans+=o.pop(0)
    ans+=e.pop(0)
if o:
    ans+=o.pop(0)
print(ans)