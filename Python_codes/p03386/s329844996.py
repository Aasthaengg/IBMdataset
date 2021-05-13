a,b,k = map(int, input().split())
ans = []
if b-a < 2*k:
    ans = list(range(a,b+1))
else:
    ans = [a+i for i in range(k)] + [b-i for i in reversed(range(k))]
print('\n'.join(map(str, ans)))