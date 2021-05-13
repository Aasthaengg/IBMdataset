import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

r,d,x0=MI()
answers=[]
x=x0
for i in range(10):
    x=r*x-d
    answers.append(x)
#print(answers)
for ans in answers:
    print(ans)