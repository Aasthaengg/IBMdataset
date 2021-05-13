mass=int(input())
number=list(map(int,input().split()))

cnt = 0

for i in range(mass):
    if (i+1)%2!=0 and number[i]%2!=0:
        cnt+=1

print(cnt)