from statistics import median
n = int(input())
A = list(map(int,input().split()))
A = [a-i-1 for i,a in enumerate(A)]
A.sort()
mA = int(median(A))
print(min([sum([abs(a-mA-1) for a in A]), sum([abs(a-mA) for a in A]), sum([abs(a-mA+1) for a in A])]))