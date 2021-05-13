n = int(input())
str = input().split()
a_i = []
for x in range(n):
    a_i.append(int(str[x]))
a_i.sort()
print(a_i[n - 1] - a_i[0])