n = int(input())
a_list = list(map(int, input().split()))

sorted_a = sorted(a_list)

print(sum(sorted_a[n:3*n:2]))