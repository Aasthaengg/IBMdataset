n = int(input())
s = list(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))

count = 0
for i in range(len(t)):
    if t[i] in s:
        count += 1
print(count)