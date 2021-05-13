s = input()
t = input()

ans = False
for _ in range(len(s)):
    l = list(s)
    c = l.pop(-1)
    l.insert(0, c)
    s = ''.join(l)
    
    # print(s)
    if s == t:
        ans = True
        break
    
if ans:
    print('Yes')
else:
    print('No')