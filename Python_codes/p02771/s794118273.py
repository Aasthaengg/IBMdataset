A, B, C = map(int, input().split())
print('Yes' if (A == B and A != C) or (A == C and A != B) or (B == C and A != B) else 'No')
