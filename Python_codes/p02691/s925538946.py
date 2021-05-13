import collections
n = int(input())
a_list = list(map(int,input().split()))
a_list2 = [i-a for i,a in enumerate(a_list)]
a_list_dic = collections.Counter(a_list2)
count = 0
for i,a in enumerate(a_list):
    a_list_dic[i-a] -= 1
    count += a_list_dic[i+a]

print(count)