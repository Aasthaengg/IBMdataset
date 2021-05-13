n = int(input())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))
list_sa = [abs(x_list[i] - y_list[i]) for i in range(n)]
list_sa2 = [pow(i, 2) for i in list_sa]
list_sa3 = [pow(i, 3) for i in list_sa]
print(sum(list_sa))
print(pow(sum(list_sa2), 1/2))
print(pow(sum(list_sa3), 1/3))
print(max(list_sa))
