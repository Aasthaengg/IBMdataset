n = int(input())
a_list = [0] + list(map(int, input().split()))
b_list = [0] + list(map(int, input().split()))
c_list = [0] + list(map(int, input().split()))

sum = 0

for i in range(1, n+1):
    sum += b_list[a_list[i]]
    if i >= 2:
        if a_list[i] == a_list[i-1] + 1:
            sum += c_list[a_list[i-1]]
    #print(sum)


print(sum)