N=int(input())
A=map(int, input().split())
S=0
for a in A:
  S+=1/a
print(1/S)