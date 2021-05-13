a = list(map(int, input().split()))
maxNum = max(a)
a.remove(maxNum)
total = a[0] + a[1]
if total == maxNum: 
    print("Yes")
else: 
    print("No")
