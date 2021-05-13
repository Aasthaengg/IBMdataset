n=int(input())
plist=list(map(int,input().split()))

counter  = 0
for i in range(n):
    if plist[i] != i + 1:
        counter += 1

if counter == 0 or counter == 2:
    print("YES")
else:
    print("NO")