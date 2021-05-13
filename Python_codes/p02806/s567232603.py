n = int(input())
name = []
time = []
for i in range(n):
    a,b = input().split()
    name.append(a)
    time.append(b)
count = 0
for i in range(name.index(input()) + 1,n):
    count += int(time[i])
print(count)