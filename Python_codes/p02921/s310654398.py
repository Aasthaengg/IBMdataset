s = input()
t = input()
cnt = 0
for x, y in zip(s,t):
    if x == y:
        cnt+=1
print(cnt)