N=int(input())
A=tuple(map(int,input().split()))

sum = 1
for a in A:
  if a%2 == 0:
    sum *= 2

print(3**N-sum)