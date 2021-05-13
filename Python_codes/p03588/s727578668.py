n = int(input())
a, b = 0, 0
for i in range(n):
    a_input, b_input = map(int, input().split())
    if a < a_input:
        a, b = a_input, b_input
print(a + b)