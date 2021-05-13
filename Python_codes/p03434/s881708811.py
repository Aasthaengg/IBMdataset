n = int(input())

a_list = list(map(int, input().split()))
# print(a_list)

a_list = sorted(a_list, reverse=True)
# print(a_list)

alice = 0
bob = 0
for i in range(len(a_list)):
    if i % 2 == 0:
        alice += a_list[i]
    else:
        bob += a_list[i]
print(alice - bob)