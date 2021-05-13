s= input()
g = 'gp'*(len(s)//2)+'g'*(len(s)%2)
cnt = 0
for si,gi in zip(s,g):
    if si == gi:
        continue
    elif si =='g' and gi == 'p':
        cnt += 1
    else:
        cnt -= 1
print(cnt)
