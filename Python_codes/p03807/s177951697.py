n = int(input())
a_list = list(map(int, input().split()))

num_of_odd = 0
for a in a_list:
    if a % 2 == 1:
        num_of_odd += 1
if num_of_odd % 2 == 0:
    print("YES")
else:
    print("NO")
