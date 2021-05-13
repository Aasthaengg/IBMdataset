X = int(input())

if X > 1:
    line = input()
    v_inputs = [int(n) for n in line.split()]

    line = input()
    numbers = [int(n) for n in line.split()]
else:
    v_inputs = [int(input())]
    numbers = [int(input())]

cost_values = [
                gem_value - gem_cost
                for gem_value, gem_cost in zip(v_inputs, numbers)]
predicted_value = 0
for cost_value in cost_values:
    if cost_value > 0:
        predicted_value += cost_value

print(predicted_value)
