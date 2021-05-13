n=int(input())

t=int(2*n**0.5)
ans = {i for i in range(1,t+1)}

sum=t*(t+1)//2


for i in range(t,0,-1):
    if sum-i >n:
        ans.remove(i)
        sum -= i
    elif sum-i == n:
        ans.remove(i)
        break

for i in ans:
    print(i)
