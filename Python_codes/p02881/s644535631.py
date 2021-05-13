n = int(input())
lists = []
for i in range(1, int(n** 0.5 + 1)):
    if n % i ==0:
        lists.append(i + n/i)
print(int(min(lists)) - 2)