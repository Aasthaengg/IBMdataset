n = int(input())
a = list(map(int, input().split()))
a_dict = {}
for i, value in enumerate(a):
    a_dict[i+1] = value
print(*[key for key, value in sorted(a_dict.items(), key=lambda k:k[1])])