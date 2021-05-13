import sys
n = int(input())
print(0, flush=True)
f, m = "Female", "Male"
s = input()
if s == "Vacant":
    quit()
x = 0 if s == f else 1
high = n-1
low = 0
while high - low > 1:
    mid = (high + low) // 2
    print(mid, flush=True)
    s = input()
    if s == "Vacant":
        sys.exit()
    if mid % 2 == x:
        if s == f:
            low = mid
        else:
            high = mid
    else:
        if s == f:
            high = mid
        else:
            low = mid
print(high, flush=True)
sys.exit()