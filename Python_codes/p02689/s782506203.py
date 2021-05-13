#n = int(input())
n, m = map(int, input().split())
hl = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

isgood = [True for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    if hl[a-1] <= hl[b-1]:
        isgood[a-1] = False
    if hl[b-1] <= hl[a-1]:
        isgood[b-1] = False
print(isgood.count(True))
