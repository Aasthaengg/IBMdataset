import collections
s  = list(input())
n = len(s)
alp = "abcdefghijklmnopqrstuvwxyz"
alp = list(alp)
co_alp = collections.Counter(alp)
if n==26:
    for i in range(n-1):
        if s[-i-1] >s[-i-2]:
            q = "z"
            for sj in s[-i-1:]:
                if sj >s[-i-2]:
                    q = min(q,sj)
            l = s[:-i-2]
            l.append(q)
            print("".join(l))
            break
    else:
        print(-1)
    exit()

for i in range(n):
    co_alp[s[i]]+=1
for w,num in sorted(co_alp.items()):
    if num==1:
        s.append(w)
        break
print("".join(s))
