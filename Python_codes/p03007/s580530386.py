n=int(input())
a = list(map(int, input().split()))

a.sort()

absum=0
minabs=10**9
for num in a:
        abnum=abs(num)
        absum+=abnum
        if minabs > abnum:
                minabs=abnum

if a[0] <= 0 and a[-1] >=0:
        print(absum)
else:
        print(absum - 2*minabs)
        num1=a.pop(0)
        num2=a.pop(-1)
        if abs(num1) > abs(num2):
                print(num2,num1)
                a.append(num2-num1)
        else:
                print(num1,num2)
                a.append(num1-num2)
a.sort()
#print(a)

now = a[0]
for i in range(len(a)-2,-1,-1):
        if a[i] > 0:
                print(now, a[i])
                now-=a[i]
#print(now)
a[0]=now

now = a[-1]

for i in range(len(a)-1):
        if a[i] >0:
                break
        print(now,a[i])
        now-=a[i]