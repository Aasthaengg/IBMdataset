n=int(input())
a_list=[int(s)-(i+1) for i,s in enumerate(input().split())]
a_list.sort()

total=0
for i in a_list:
    total+=abs(i-a_list[n//2])
print(total)