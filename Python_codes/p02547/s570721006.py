def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

n = NextInt()
da = [NextIntList() for i in range(n)]
cnt, ans = 0, 0
for i in range(n):
    if(da[i][0] == da[i][1]):
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)
if ans >= 3:
    print('Yes')
else:
    print('No')