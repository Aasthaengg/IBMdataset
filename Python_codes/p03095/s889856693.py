
n = int(input())
s = list(input())
t = []
ans = 1
count= []

t = set(s)
t = list(t)

for i in range(len(t)):
    count.append(s.count(t[i]))

for j in range(len(count)):
    ans *= (count[j] + 1)

print((ans-1)%(10**9 + 7))
