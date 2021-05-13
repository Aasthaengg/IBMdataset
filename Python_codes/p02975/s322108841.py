n = int(input())
a = list(map(int, input().split()))

res=0
a_set=set(a)

res=0
for i in range(n):
    res = res ^ a[i]

if n % 3 ==0:
    if res==0:
        print("Yes")
        exit()
else:
    if len(a_set) ==1:
        print("Yes")
        exit()
print("No")