num=list(map(int,input().split()))
num.sort()
ans=0
print(abs(num[0]-num[1])+abs(num[1]-num[2]))