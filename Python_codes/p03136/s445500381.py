s = int(input())
lst = list(map(int,input().split()))
lst.sort()

if lst[-1] < sum(lst[:-1]):
    print("Yes")
else:
    print("No")
