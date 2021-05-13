inputs = []
while True:
    try:
        inputs.append(int(input()))
    except(EOFError):
        break

inputs.pop(0)

minv = inputs[0]
maxv = inputs[1] - inputs[0]

for i in range(1, len(inputs)):
    maxv = max([maxv, inputs[i] - minv])
    minv = min([minv, inputs[i]])

print(maxv)



