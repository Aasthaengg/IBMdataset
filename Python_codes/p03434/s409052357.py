N=int(input())
li=list(map(int, input().split()))
li.sort(reverse=True)
Alice=[]
Bob=[]

for i in range(N):
  if i%2==0:
    Alice.append(li[i])
  else:
    Bob.append(li[i])

print(sum(Alice)-sum(Bob))