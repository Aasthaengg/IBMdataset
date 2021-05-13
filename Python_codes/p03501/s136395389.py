num = list(map(int,input().split()))
t = num[0]*num[1]
if t <= num[2]:
    print(t)
else:
    print(num[2])
