N = int(input())
s = ['']*N
t = ['']*N
for i in range(N):
    s[i], t[i] = input().split()
t = list(map(int, t))
t.append(0)
x = input()

for i in range(N):
    if s[i] == x:
        idx = i
        break

print(sum(t[idx+1:]))