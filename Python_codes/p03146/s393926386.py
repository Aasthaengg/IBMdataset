# 初期入力
import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
a+= [0]*(10**6 +1)
i=0
while True:
   
    if a[i] %2 ==0:
        a[i+1] =a[i]//2
    else:
        a[i+1] =a[i] *3 +1
    if a[i+1] in a[:i]:
        print(i+1+1)
        break
    i +=1