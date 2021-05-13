import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
l = [chr(v) for v in range(ord("a"), ord("z")+1)]
l2 = {c:i for i,c in enumerate(l)}
def sub(s1, s2, used):
#     print(s1,s2,used)
    if not s1:
        if s2[0]=="z":
            return -1
        else:
            return l[l2[s2[0]]+1]
    if len(s1)+len(s2)<26:
        for i in range(26):
            if l[i] not in used:
                return s1+l[i]+s2
    else:
        if not s2:
            return sub(s1[:-1], s1[-1], set(s1[:-1]))
        for i in range(l2[s2[0]]+1, 26):
            if l[i] not in used:
                ans = s1+l[i]
#                 used.add(l[i])
#                 ans = ans + "".join(sorted([c for c in l if c not in used]))
                return ans
        used.remove(s1[-1])
        return sub(s1[:-1], s1[-1]+s2, used)
ans = sub(s, "", set(s))
print(ans)