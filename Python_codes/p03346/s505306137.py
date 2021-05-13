n = int(input())
lst = [0]*(n+1)
for i in range(n):
    lst[int(input())] = i
s = 0
t = 1
for i in range(1,n):
    if lst[i] < lst[i+1]:
        t += 1
    else:
        s = max(t,s)
        t = 1
s = max(t,s)
print(n-s)