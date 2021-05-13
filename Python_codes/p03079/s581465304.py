from sys import stdin
A, B, C = [int(x) for x in stdin.readline().rstrip().split()]

if A==B==C:
   print("Yes")
else:
   print("No")