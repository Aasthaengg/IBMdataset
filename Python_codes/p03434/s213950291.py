n = int(input())
a_list = list(map(int, input().split()))
alice = 0
bob = 0
a_list.sort(reverse=True)
i = 0
for a_i in a_list:
  if i % 2 == 0:
    alice += a_i
  else:
    bob += a_i
  i += 1
print(alice - bob)