n,k= map(int, input().split())
num= [int (x) for x in input().split()]
for i in range(n-k):
    if num[i] < num[k+i]:
        print("Yes")
    else:
        print("No")