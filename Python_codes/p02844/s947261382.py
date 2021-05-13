_ = input()
s = list(input())
cnt = 0
for i in range(1000):
    a = list(f'{i:03}')
    if a[0] not in s: continue
    s1 = s[s.index(a[0])+1:]
    if a[1] not in s1: continue
    s1 = s1[s1.index(a[1])+1:] 
    if a[2] not in s1: continue
    cnt += 1
print(cnt)