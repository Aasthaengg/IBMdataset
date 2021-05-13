N = int(input())

Alice = []
Bob = []

a = list(map(int, input().split()))
a.sort(reverse=True)

if len(a) % 2 == 1:
    a.append(0)

while len(a) > 0:
    Alice.append(a.pop(0))
    Bob.append(a.pop(0))

print(sum(Alice) - sum(Bob))