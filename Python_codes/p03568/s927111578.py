n=int(input())
a = len([int(i) for i in input().split() if int(i)%2==0])
print(3**n-2**a)