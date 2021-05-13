n = int(input())
s = set(filter(lambda x : n % x == 0 and n / x < 10, [x for x in range(1, 10)]))
print("No" if len(s) == 0 else "Yes")