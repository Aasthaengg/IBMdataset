n = int(input())
a = list(map(int, input().split()))
a_suseki = 1
a_nukewa = 0

for i in range(n):
  a_suseki = a_suseki * a[i]

for i in range(n):
  a_nukewa = a_nukewa + (a_suseki/a[i])

print(a_suseki / a_nukewa)