a = int(input())
b = int(input())
c = int(input())
x = int(input())
answer_values = []

for a_value in range(a + 1):
    for b_value in range(b+1):
        for c_value in range(c+1):
            answer_values.append(a_value * 500 + b_value * 100 + c_value * 50)

print(answer_values.count(x))