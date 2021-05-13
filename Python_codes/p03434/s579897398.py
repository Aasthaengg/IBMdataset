N = int(input())
int_list = list(map(int, input().split()))

int_list.sort(reverse=True)
odd = int_list[::2]
even = int_list[1::2]
print(sum(odd)-sum(even))