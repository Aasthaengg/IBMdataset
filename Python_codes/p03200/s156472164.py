s = input()
N = len(s)
sl = [0]*N
cnt = 0
for i in range(N):
    if s[i]=='B':
        cnt+=1
    else:
        sl[i] = cnt
print(sum(sl))