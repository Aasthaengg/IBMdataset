import sys

n = int(input())
dn = list(map(int, input().split()))
m = int(input())
tn = list(map(int, input().split()))

num_dict = {}

for i in range(n):
    if str(dn[i]) in num_dict.keys():
        num_dict[str(dn[i])] += 1
    else:
        num_dict[str(dn[i])] = 1

for i in range(m):
    if str(tn[i]) in num_dict.keys():
        num_dict[str(tn[i])] += -1
    else:
        print("NO")
        sys.exit()

result_list = list(num_dict.values())
for i in range(len(result_list)):
    if result_list[i] < 0:
        print("NO")
        sys.exit()
print("YES")