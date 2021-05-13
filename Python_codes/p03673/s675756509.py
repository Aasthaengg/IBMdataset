N = int(input())
A = list(map(int,input().split()))
A_odd = A[1::2]
A_even = A[::2]
if N%2 !=0:
 A_even = A_even[::-1]
 ans = A_even + A_odd
 for s in ans:
  print(s, end =" ")
else:
 A_odd = A_odd[::-1]
 ans = A_odd + A_even
 for s in ans:
  print(s, end =" ")