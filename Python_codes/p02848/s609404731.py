A = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
N = int(input())
S = input()

s = ""
for c in S:
  new_index = (A.index(c) + N) % 26
  s += A[new_index]
  
print(s)