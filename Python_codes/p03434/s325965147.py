n = int(input())
argList = list(map(int, input().split()))
argList.sort()
argList.reverse()
a=0
b=0

for i in range(0, n):
    if i % 2 == 0:
        a+=argList[i]
    else:
        b+=argList[i]
print(a-b)