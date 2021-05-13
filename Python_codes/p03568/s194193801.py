N=int(input())
A=list(map(int, input().split(" ")))

evencount=0
for a in A:
  if a%2==0:
    evencount=evencount+1

print(3**N-2**(evencount))