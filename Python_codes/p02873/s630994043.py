S = input()

def count_ll(l):

    ret = [0]
    cur = 0

    for c in l:
        if c == "<":
            cur += 1
        else:
            cur = 0
        
        ret.append(cur)
    
    return ret

def count_rg(l):

    revl = reversed(l)
    ret = [0]
    cur = 0

    for c in revl:
        if c == ">":
            cur += 1
        else:
            cur = 0
        
        ret.append(cur)
    
    return list(reversed(ret))

l = count_ll(S)
r = count_rg(S)
# print("left: >", l)
# print("right: <", r)

N = len(S) + 1

ans = 0
for i in range(N):
    ans += max(l[i], r[i])

print(ans)

