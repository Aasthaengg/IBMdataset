import sys
n = int(input())

print(0)
sys.stdout.flush()
s = input()

if s == "Vacant":
    exit()

low = 1
high = n-1
tmp = 0
cnt = 1

while low+1 < high:
    mid = (low + high) //2
    
    print(mid)
    sys.stdout.flush()
    t = input()
    cnt += 1
    
    if mid % 2 == 0:
        if t[0] == s[0]:
            low = mid
        elif t[0] == "V":
            exit()
        else:
            high = mid
    else:
        if t[0] == s[0]:
            high = mid
        elif t[0] == "V":
            exit()
        else:
            low = mid

print(high)
sys.stdout.flush()
s = input()
if s[0] == "V":
    exit()
else:
    print(low)
    sys.stdout.flush()
    s = input()
    exit()