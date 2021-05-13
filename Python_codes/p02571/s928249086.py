def comp(a,b):
    s = 0
    for i,j in zip(a,b):
        if not i == j:
            s += 1
    return s
 
s = input()
t = input()
ans = len(t)
 
for i in range(len(s) - len(t) + 1):
    score = comp(s[i:i+len(t)],t)
    if score == 0:
        ans = score
        break
    if ans > score:
        ans = score
 
print(ans)