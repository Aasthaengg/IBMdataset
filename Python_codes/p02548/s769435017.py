def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

n = NextInt()
ans = 0
for i in range(1, n):
    now = i
    while now < n:
        now += i
        ans += 1
print(ans)