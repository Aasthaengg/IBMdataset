N = int(input())
A = [int(a) for a in input().split()]
odd = 0
for i, a in enumerate(A):
  odd += a % 2
print("YES" if odd % 2 == 0 else "NO")