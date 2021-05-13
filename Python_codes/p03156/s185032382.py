n = int(input())
a, b = map(int, input().split())
p = [int(i) for i in input().split()]
p_a = len([i for i in p if i <= a])
p_a_b = len([i for i in p if a < i <= b])
p_b = n - p_a - p_a_b
print(min(min(p_a, p_b), p_a_b))