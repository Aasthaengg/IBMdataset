n = int(input())
l = input().split(" ")
for i in range(len(l)):
    l[i] = int(l[i])

l.sort(reverse=True)
sum = 0
for i in range(1, n):
    sum += l[i]

if sum > l[0]:
    print("Yes")
else:
    print("No")
