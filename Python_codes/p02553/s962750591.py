def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

a,b,c,d = MI()
print(max(a*c,a*d,b*c,b*d))