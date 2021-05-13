n = int(input())
li = list(map(int, input().split()))

for i in range(n-1):
    if li[i] > li[i+1]:
        li[i+1] += 1

if any(li[i] > li[i+1] for i in range(n-1)):
    print("No")
else:
    print("Yes")