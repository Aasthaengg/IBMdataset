n = int(input())
import sys

def ato(x):
    if x == "Male":
        return 0
    elif x == "Female":
        return 1
    else:
        return -1
    
print(0)
s0 = ato(input())
if s0 == -1:
    sys.exit()
    
print(n-1)
s1 = ato(input())
if s1 == -1:
    sys.exit()
    
left = 0
right = n-1
center = (left+right) // 2
while True:
    center = (left+right) // 2
    
    print(center)
    s2 = ato(input())
    if s2 == -1:
        break
    
    if (center - left)%2 == abs(s2 - s0):
        left = center
        s0 = s2
    else:
        right = center
        s1 = s2