n=int(input())
a_list=list(map(int,input().split()))
for i in range(n):
    a_list[i]=a_list[i]-(i+1)
a_list.sort()
b=a_list[n//2]
Sum=0
for i in a_list:
    Sum=Sum+abs(i-b)
print(Sum)
