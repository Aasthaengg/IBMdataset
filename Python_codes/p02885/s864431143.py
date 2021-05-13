def ri(): return int(input())
def rli(): return list(map(int, input().split()))
def rls(): return list(map(str, input().split()))
def pl(a): print(" ".join(list(map(str, a))))
def ma():return map(int,input().split())

a,b=ma()
if a>2*b:
  print(a-2*b)
else: 
  print(0)