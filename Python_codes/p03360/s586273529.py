abc_list = list(map(int,input().split()))
k = int(input())
abc_list.sort()
for i in range(k):
    abc_list[2] = abc_list[2] * 2
print(sum(abc_list))