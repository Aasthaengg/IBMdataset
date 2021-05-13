n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(n-2):
    l = p[i:i+3]
    ls = sorted(l)
    if l[1] == ls[1]:
        count += 1
print(count)
