N = int(input())
people = [int(i) for i in input().split()]
step = 0
front = people[0]
for i in range(N):
    if front > people[i]:
        step += front - people[i]
    else:
        front = people[i]
print(step)