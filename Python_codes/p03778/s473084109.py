w, a, b = map(int, input().split())
right = min(a, a+w, b, b+w)
left = max(a, a+w, b, b+w)

if 2 * w >= left - right:
    print(0)
else: 
    print(left - right - 2 * w)