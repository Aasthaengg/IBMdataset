n = int(input())
a = [int(input())%2==1 for _ in range(n)]
if sum(a)==0:
    print("second")
else:
    print("first")