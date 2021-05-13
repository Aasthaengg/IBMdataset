n = input()
 
A = list(map(int, input().split()))
 
counts = 0
while all(a%2==0 for a in A):
  A = [a/2 for a in A]
  counts += 1
print(counts)