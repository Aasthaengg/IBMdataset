n = int(input())
a = [int(x) for x in input().split(" ")]
s = [0]

for x in range(1, n):
    stool = max(a[x - 1] - a[x], 0)
    s.append(stool)
    a[x] += stool
    
print(sum(s))