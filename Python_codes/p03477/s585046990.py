A, B, C, D = map(int, input().split())
print("Right" if (A+B) < (C+D) else "Balanced" if (A+B) == (C+D) else "Left")