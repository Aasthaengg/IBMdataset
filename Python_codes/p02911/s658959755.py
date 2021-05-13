#C
n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
people = [0] * n
for i in a:
    people[i-1] += 1
# print(people)
for i in people:
    if k <= q - i:
        print("No")
    else:
        print("Yes")