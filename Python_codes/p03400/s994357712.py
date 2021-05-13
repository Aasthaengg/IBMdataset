n = int(input())
d, x = [int(s) for s in input().split()]
a_list = [int(input()) for _ in range(n)]
print(sum([(d - 1) // a + 1 for a in a_list]) + x)