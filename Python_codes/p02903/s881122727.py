h,w,a,b = map(int,input().split())
ans = []
for _ in range(h-b):
    l = '0' * (w-a) + '1' * a
    ans.append(l)
for _ in range(b):
    l = '1' * (w-a) + '0' * a
    ans.append(l)
for i in range(h):
    print(''.join(ans[i]))