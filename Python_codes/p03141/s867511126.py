import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
ABC= []
for _ in range(N):
    a,b = map(int,input().split())
    ABC.append([a,b,a+b])

taka = 0
aoki = 0
ABC.sort(key=lambda x:x[2])
while ABC:
    
    taka += ABC.pop()[0]
    if len(ABC)==0:
        break
    aoki += ABC.pop()[1]
print(taka-aoki)
