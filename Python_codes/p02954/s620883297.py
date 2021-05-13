S = input()
seq = [1]
pos = []
for i,(a,b) in enumerate(zip(S,S[1:])):
    if a+b == 'RL':
        pos.append(i)
    if a==b:
        seq[-1] += 1
    else:
        seq.append(1)

ans = [0] * len(S)
for r,l,p in zip(seq[::2],seq[1::2],pos):
    ans[p] = ans[p+1] = (r+l)//2
    if (r+l)%2:
        if r > l:
            ans[p] += 1
        else:
            ans[p+1] += 1
        if max(r,l)%2==0:
            ans[p],ans[p+1] = ans[p+1],ans[p]
print(*ans)