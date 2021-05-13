k,n = map(int, input().split())
a = list(map(int, input().split()))

kyori=[0]*len(a)

for i in range(1,len(a)):
    kyori[i]=a[i]-a[i-1]

kyori[0]=a[0]+k-a[-1]

print(sum(kyori)-max(kyori))