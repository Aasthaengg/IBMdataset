A, B, C, D = map(int, input().split())
print('Balanced') if (A + B) == (C + D) else print('Left' if (A + B) > (C + D) else 'Right')