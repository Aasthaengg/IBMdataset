r, g, b = map(int, input().split())
k = int(input())
count = 0
while g<=r: g*=2; count+=1
while b<=g: b*=2; count+=1
if count<=k: print('Yes')
else: print('No')