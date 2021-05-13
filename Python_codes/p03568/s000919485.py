N = int(input())
A = [int(i) for i in input().split()]
ans = 3**N
even = 0
for a in A:
  if a%2==0:
    even += 1
    
print(ans-2**even)