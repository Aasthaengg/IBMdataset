d,g = map(int,input().split())
probs = []
for i in range(d):
    p,c = map(int,input().split())
    probs.append([p,c])

probs.reverse()

#compするかどうかは2^10全通りに対して残ったやつからコンプしないように高い順にとってくのが最適
def tobin(x, n):
    return format(x, 'b').zfill(n)

ans = 1e9
for i in range(2**d):
    s = tobin(i,d)
    comp = [c=="1" for c in s]
    tmp = 0
    cos = 0
    for j in range(d):
        if comp[j]:
            tmp += probs[j][0]*(d-j)*100+probs[j][1]
            cos += probs[j][0]

    for j in range(d):
        if comp[j]:
            continue
        else:
            if tmp < g:
                mc = (probs[j][0]-1)*(d-j)*100

                if mc + tmp >= g:
                    rest = g-tmp
                    cos += (g-tmp)//((d-j)*100)
                    if (g-tmp)%((d-j)*100) == 0:
                        break
                    else:
                        cos += 1
                        break
                else:
                    cos += probs[j][0]
                    tmp += mc
            else:
                break
    if ans > cos:
        ans = cos

print(ans)



