n = int(input())
a = list(map(int, input().split()))

a_xor = 0
for ai in a:
  a_xor ^= ai

print(" ".join([str(ai ^ a_xor) for ai in a]))