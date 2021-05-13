n = int(input())
a_list = list(map(int,input().split()))

a_dict = {}

for a in a_list:
    if a not in a_dict:
        a_dict[a] = 1
    else:
        a_dict[a] += 1

values = list(a_dict.values())
double = sum(values) - len(values)
# print(values,double)

print(len(a_list) - (double//2 + double%2)*2)