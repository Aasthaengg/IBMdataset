n = int(input())
left = 0
right = n
print(left)
sl = input()
if sl[0] == "V":
    quit()
while True:
    mid = (left + right) // 2
    print(mid)
    sm = input()
    if sm[0] == "V":
        quit()
    if ((mid - left) % 2 == 1) ^ (sl == sm):
        left = mid
        sl = sm
    else:
        right = mid
