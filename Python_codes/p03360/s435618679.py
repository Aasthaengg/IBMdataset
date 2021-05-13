MM = input().split()
A = int(MM[0])
B = int(MM[1])
C = int(MM[2])
K = int(input())
S = [A,B,C]
S.sort()

S[-1] = S[-1] * 2 ** K

total =0
for i in S:
  total += i
print(total)