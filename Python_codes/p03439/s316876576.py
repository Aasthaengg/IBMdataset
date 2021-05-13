N = int(input())
mid = (N-1)//2

print(mid)
s = input()
if s == "Vacant":
    exit()
else:
    mid_state = s

print(0)
s = input()
if s == "Vacant":
    exit()
elif (mid % 2 == 0 and mid_state != s) or (mid % 2 != 0 and mid_state == s):
    l, r, l_state = 0, mid, s
else:
    l, r, l_state = mid, N, mid_state

while True:
    if (r - l) % 2 != 0:
        i = (r-l+1)//2 + l
    else:
        i = (r-l)//2 + l
    print(i)
    s = input()
    if s == "Vacant":
        exit()
    elif ((i-l) % 2 == 0 and l_state != s) or ((i-l) % 2 != 0 and l_state == s):
        r = i
    else:
        l, l_state = i, s
