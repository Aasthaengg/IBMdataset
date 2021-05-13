h,n = input().split()
a = list(map(str,input().split()))
attack = 0
for i in range(int(n)):
    attack += int(a[i])
if int(h) - attack <= 0:
    print("Yes")
else:
    print("No")