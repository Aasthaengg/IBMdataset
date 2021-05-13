N = int(input())
S, T = input().split()
ans = [0]*(N*2)
Scount = 0
Tcount = 1
for i in S:
    ans[Scount] = i
    Scount += 2
for j in T:
    ans[Tcount] = j
    Tcount += 2

print(''.join(ans))
