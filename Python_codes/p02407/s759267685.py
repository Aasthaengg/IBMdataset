n = int(input())
n_list = [int(i) for i in input().split(" ")]
n_list.reverse()
print(' '.join(map(str, n_list)))