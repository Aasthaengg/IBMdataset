A, B, C, D = map(int, input().split())
left = A + B
right = C + D

if (left > right):
    ans = 'Left'
elif (left == right):
    ans = 'Balanced'
else:
    ans = 'Right'

print(ans)