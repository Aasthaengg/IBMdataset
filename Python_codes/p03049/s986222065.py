#-----------------------------
#https://atcoder.jp/contests/agc008/submissions/15248942
import sys
 
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))
#-----------------------------
N = ini()
ans = 0
lastA = 0
firstB = 0
BA = 0

for i in range(N):
    s = input()
    #siの文字列内のABを抽出
    for j in range(len(s)-1):
        if s[j:j+2] == "AB":
            ans += 1

    #先頭Bかつ末尾A、先頭B、末尾A、を抽出
    if s[0] == "B" and s[-1] == "A":
        BA += 1
    elif s[0] == "B":
        firstB += 1
    elif s[-1] == "A":
        lastA += 1

if BA >= 2:
    ans += BA - 1

#BAと末尾Aと先頭Bをつなげて、余った末尾Aと先頭Bをつなげる
if BA >= 1 and lastA >= 1 and firstB >=1:
    ans += 2 + min(lastA-1,firstB-1)
#BAと末尾Aをつなげる
elif BA >= 1 and lastA >= 1 and firstB == 0:
    ans += 1
#BAと先頭Bをつなげる
elif BA >= 1 and lastA == 0 and firstB >= 1:
    ans += 1
#末尾Aと先頭Bをつなげる
elif BA < 1 and lastA >= 1 and firstB >= 1:
    ans += min(lastA,firstB)

print(ans)
