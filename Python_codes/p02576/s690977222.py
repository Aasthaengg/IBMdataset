# string
# a, b, c = input().split()
# str_list = list(input().split())

# number
# a, b, c = map(int, input().split())
# num_list = list(map(int, input().split()))

# lows
# str_list = [input() for _ in range(n)]

# many inputs
# num_list = []
# for i in range(n): num_list.append(list(map(int, input().split())))

n, x, t = map(int, input().split())

a = int((n+x-1)/x)
print(t*a)