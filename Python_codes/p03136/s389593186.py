N = int(input())
l = list(map(int,input().split()))

max = max(l)
sum = sum(l)
    
if max >= sum - max:
    print("No")
else:
    print("Yes")