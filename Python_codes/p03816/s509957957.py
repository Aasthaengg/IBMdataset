n = int(input())
a = list(map(int, input().split()))

eat = n - len(list(set(a)))
if eat % 2 == 1:
    eat += 1
print(n - eat)
