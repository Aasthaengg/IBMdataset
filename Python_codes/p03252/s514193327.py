import collections as col
 
s = list(input())
t = list(input())
 
c1 = col.Counter(s)
c2 = col.Counter(t)
 
cv1 = sorted(c1.values())
cv2 = sorted(c2.values())
 
if cv1 == cv2:
    print('Yes')
else:
    print('No')
