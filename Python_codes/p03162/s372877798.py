n = int(input())
h_list = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b, c = [int(x) for x in input().split()]
    h_list[i][0] = a + max(h_list[i - 1][1], h_list[i - 1][2])
    h_list[i][1] = b + max(h_list[i - 1][0], h_list[i - 1][2])
    h_list[i][2] = c + max(h_list[i - 1][0], h_list[i - 1][1])
print(max(h_list[n]))