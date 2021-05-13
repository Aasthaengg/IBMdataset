n = int(input())
a_list = [int(input()) for _ in range(n)]
b_list = sorted(a_list, reverse=True)
for a in a_list:
    print(b_list[0] if a != b_list[0] else b_list[1])