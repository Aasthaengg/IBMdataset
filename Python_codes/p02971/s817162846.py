n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

copy =  num_list.copy()
copy.sort()
maximum = copy[-1]
second = copy[-2]

for i in num_list:
    if i == maximum:
        print(second)
    else:
        print(maximum)