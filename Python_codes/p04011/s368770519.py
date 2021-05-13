n = int(input())
k = int(input())
x = int(input())
y = int(input())
bill = 0
for i in range(1,n+1):
    if i <= k:
        bill += x
    if i > k:
        bill +=y
print(bill)

