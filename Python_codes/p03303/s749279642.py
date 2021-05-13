s = input()
w = int(input())
ans = ''
for i,si in enumerate(s):
    if i % w == 0: ans += si
print(ans)