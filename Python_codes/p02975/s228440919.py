from collections import Counter

N = int(input())
*a, = map(int, input().split())
c = Counter(a)
used = set(c.keys())
size = len(used)

def check():
    if 0 in used:
        if size==1 or (size==2 and c[0]==N//3):
            return True
    elif size==3:
        s, t, u = used
        if s^t^u==0 and c[s]==c[t]==c[u]:
            return True
    return False

print("Yes" if check() else "No")