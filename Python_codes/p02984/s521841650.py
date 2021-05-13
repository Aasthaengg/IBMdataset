def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))

N = i()
A = l()
num = sum(A)//2
A += A
ans = []
for i in range(1):
    num2 = 0
    for j in range(0,N,2):
        num2 += A[i+j]
    ans.append(abs((num-num2))*2)
    r = abs((num-num2))*2
for i in range(1,N):
    r = A[i-1]*2-r
    ans.append(r)
print(*ans)