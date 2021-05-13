from collections import Counter

N = int(input())
*a, = map(int, input().split())
c = Counter(a)
used = set(c.keys())
size = len(used)

if 0 in used and size==1:
    print("Yes")
elif 0 in used and size==2 and c[0]==N//3:
    print("Yes")
elif size==3:
    s, t, u = used.pop(), used.pop(), used.pop()
    if s^t^u==0 and c[s]==c[t]==c[u]:
        print("Yes")
    else:
        print("No")
else:
    print("No")