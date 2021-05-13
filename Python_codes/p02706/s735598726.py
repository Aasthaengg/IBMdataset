n, m = map(int, input().split())
a = list(map(int, input().split()))


answer = n - sum(a)

if answer < 0:
    print("-1")
else:
    print(answer)