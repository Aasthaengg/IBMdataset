#a問題
# x=int(input())
#
# if x>=30:
#     print("Yes")
# else:
#     print("No")

#b問題
n,d = (int(y) for y in input().split())
x=[]
count=0
for i in range(n):
    n, m = (int(y) for y in input().split())
    s=n**2+m**2
    # print(s)
    if s<=(d**2):
        count+=1
print(count)

