m,n=map(int,input().split())
hozon=[]
for i in range(n):
    hozon.append(0)
for _ in range(m):
    x = input()
    gyou = list(map(int,x.split()))
    print(x+" {0}".format(sum(gyou)))
    for num in range(n):
        hozon[num] += gyou[num]

print(" ".join(map(str,hozon))+" {0}".format(sum(hozon)))