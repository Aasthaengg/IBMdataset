import statistics
n = int(input())
a = []
for i,j in enumerate(map(int,input().split())):
  a.append(j-i-1)
b,s = statistics.median(a),0
for i in a:
  s+=abs(i-b)
print(int(s))