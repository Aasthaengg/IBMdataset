n = int(input())
memo = []
for i in range(n):
   tmp = [int(x) for x in input().split()]
   memo.append(tmp)

seat = [a[1] - a[0] + 1 for a in memo]
print(sum(seat))
