N = int(input())
li = list(map(int, input().split()))
li.sort()
a = li[N//2]
flag = True
for i in range (N//2):
    if a == li[i]:
        flag = False
if flag:
     print(li[N//2]-li[N//2-1])
else:
     print(0)