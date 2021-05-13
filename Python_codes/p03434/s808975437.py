n = int(input())
num_lists = list(map(int, input().split()))

num_lists.sort()
num_lists.reverse()
alice_num_lists = []
bob_num_lists = []

for i in range(n):
  if i%2 == 0:
    alice_num_lists.append(num_lists[i])
  else:
    bob_num_lists.append(num_lists[i])

alice_score = 0
bob_score = 0
for i in alice_num_lists:
  alice_score += i
for i in bob_num_lists:
  bob_score += i

print(alice_score - bob_score)