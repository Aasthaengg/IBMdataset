n = int(input())
A = [int(i) for i in input().split()]
empNum = {int(i):0 for i in range(1,n+1)}

for a in A: empNum[a] += 1

for v in empNum.values(): print(v)