H,W = [int(i) for i in input().split()]
a = []

for i in range(H):
    a.append(input())

print("#"*(W+2))
for i in range(H):
    print("#"+a[i]+"#")
print("#"*(W+2))