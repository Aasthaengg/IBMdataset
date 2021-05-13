inputValues = [int(i) for i in input().split()]
n = inputValues[0]
m = inputValues[1]
votes = [int(i) for i in input().split()]
total = sum(votes)
cnt = 0
for i in votes:
    if i >= total*(1/(4*m)):
        cnt += 1
        # print(i)
if cnt >= m:
    print("Yes")
else:
    print("No")
