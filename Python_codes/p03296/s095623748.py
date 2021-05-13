N = int(input())
A = [int(x) for x in input().split()]
last = 0
cnt = 0
for a in A:
    if(last==a):
        cnt+=1
        last = 0
    else:
        last = a
print(cnt)