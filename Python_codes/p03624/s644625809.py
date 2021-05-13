S = sorted(list(input()))
alphabe = list('abcdefghijklmnopqrstuvwxyz')

for s in alphabe:
    if s in S:
        continue
    else:
        ans = s
        break
else:
    ans = 'None'
    
print(ans)