N = int(input())

print(0)
left = input().rstrip("\n")
if left == "Vacant":
    exit()
print(N - 1)
right = input().rstrip("\n")
if right == "Vacant":
    exit()

even = left
odd = "Female" if even == "Male" else "Male"

left = 0
right = N - 1
while right - left > 1:
    mid = (right + left) // 2
    print(mid)
    s = input().rstrip("\n")
    if s == "Vacant":
        exit()
    
    if mid % 2 == 0:
        if even == s: # (mid, right]に空席
            left = mid + 1
        else: # [left, mid)に空席
            right = mid - 1
    else:
        if odd == s: # (mid, right]に空席
            left = mid + 1
        else: # [left, mid)に空席
            right = mid - 1

print(left)
s = input().rstrip("\n")
if s == "Vacant":
    exit()
print(right)
s = input().rstrip("\n")
if s == "Vacant":
    exit()