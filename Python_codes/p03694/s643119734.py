N = int(input().strip())
a_list = list(map(int, input().rstrip().split()))

a_list.sort()

print(a_list[-1] - a_list[0])