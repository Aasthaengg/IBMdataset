N = int(input())
num = list(map(int,input().split()))
ans = 0

for j,k in enumerate(num):
    if j % 2 ==0:
        if k % 2 !=0:
            ans +=1
        else:
            pass
    else:
        pass
print(ans)