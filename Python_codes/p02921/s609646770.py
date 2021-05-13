s = input()
t = input()

ans = 0
for ss, tt, in zip(s, t):
    if ss==tt:
        ans+=1
print(ans)