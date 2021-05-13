from collections import Counter
n = int(input())
V = list(map(int,input().split()))
cv1 = Counter(V[::2]).most_common()
cv2 = Counter(V[1::2]).most_common()
cv1.append((-1,0)); cv2.append((-1,0))
if cv1[0][0] != cv2[0][0]:
    print(n-cv1[0][1]-cv2[0][1])
else:
    print(min(n-cv1[1][1]-cv2[0][1], n-cv1[0][1]-cv2[1][1]))