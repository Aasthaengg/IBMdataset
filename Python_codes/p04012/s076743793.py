#43
import sys
w = input()
c = w.lower()
mozi = []

if w !=c:
    print("No")
    sys.exit()
    
for i in range(len(w)):
    mozi.append(w[i])
    
for i in mozi:
    if w.count(i) % 2 == 1:
        print("No")
        sys.exit()
    
print("Yes")