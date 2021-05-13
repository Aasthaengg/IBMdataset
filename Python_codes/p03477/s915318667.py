A, B, C, D = map(int, input().split())
left, right = A + B, C + D
print((
    "Left" if left > right else
    "Balanced" if left == right else
    "Right"
    ))
