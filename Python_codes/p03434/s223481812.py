N=int(input())
C=list(map(int,input().split()))
Alice=0
Bob=0
new=sorted(C,reverse=True)
for i in range(N):
  if i%2==0:
    Alice+=new[0]
    new.pop(0)
  else:
    Bob+=new[0]
    new.pop(0)
print(Alice-Bob)