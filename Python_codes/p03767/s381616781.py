N = int(input())
a = input().split()
a_i = [int(s) for s in a]
a_i.sort(reverse=True)
result = 0
for i in range(1,2 * N,2):
    result += a_i[i]
print(result)