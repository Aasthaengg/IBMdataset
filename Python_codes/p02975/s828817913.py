from collections import Counter

N = int(input())
a = [int(i) for i in input().split()]
c = Counter(a)
b = len(c.keys())

def check():
    if 0 in c.keys():
        if b==1 or (b==2 and c[0]==N//3):
            return True
    elif b==3:
        s, t, u = c.keys()
        if c[s]//3==c[t]//3==c[u]//3 and s^t^u==0:
            return True
    return False

print("Yes" if check() else "No")