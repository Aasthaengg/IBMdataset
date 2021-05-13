n = int(input())
a = list(map(int,input().split()))

a1 = sorted(a)
if((sum(a1)-a1[-1]) > a1[-1]):
    print("Yes")
else:
    print("No")