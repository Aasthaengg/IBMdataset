n = int(input())

print(0)
init_state = input().rstrip()
if init_state == "Vacant":
    exit()
if init_state == "Male":
    states = ["Male", "Female"]
else:
    states = ["Female", "Male"]

l = 0; r = n
while r - l > 1:
    mid = (r + l) // 2
    print(mid)
    new_state = input().rstrip()
    if new_state == "Vacant":
        exit()
    if new_state == states[mid % 2]:
        l = mid
    else:
        r = mid
print(r, l)