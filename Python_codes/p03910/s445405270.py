N = int(input())
Ans = []
s = 0
for i in range(1, N+1):
    Ans.append(i)
    s += i
    if s >= N:
        break

if s != N:
    Ans.remove(s-N)
for a in Ans:
    print(a)