n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l_s = sorted(l, reverse=True)

# print(l_s)

longest = l_s.pop(0)

# print(longest)
# print(l_s)

if longest < sum(l_s):
    print('Yes')
else:
    print('No')