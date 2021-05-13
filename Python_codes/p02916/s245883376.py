n = int(input())
a_list = [0] + list(map(int, input().split()))
b_list = [0] + list(map(int, input().split()))
c_list = [0] + list(map(int, input().split()))

sum = sum(b_list)

for i in range(1, n):
    if a_list[i] + 1 == a_list[i+1]:
        sum += c_list[a_list[i]]

print(sum)