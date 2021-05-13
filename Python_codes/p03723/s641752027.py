A, B, C = map(int, input().split())
X = (A|B|C)^(A&B&C)
ans = (X&-X).bit_length()-1
print(0 if (A|B|C)&1 else ans)
