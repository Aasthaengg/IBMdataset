num = int(input())
org_list = list(map(int, input().split()))

new_list = sorted(org_list, reverse=True)

alice_sum = sum(new_list[::2])
bob_sub = sum(new_list[1::2])

# print(new_list)
# print(str(alice_sum) + ":" +str(bob_sub))
print(str(alice_sum-bob_sub))