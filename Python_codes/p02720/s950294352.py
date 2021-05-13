K = int(input())

queue = list(range(1,10))
counter = 0
while counter != K - 1:
    num = queue[counter]
    ichi = num % 10
    num *= 10
    if ichi != 0:
        queue.append(num + ichi - 1)
    queue.append(num + ichi)
    if ichi != 9:
        queue.append(num + ichi + 1)
    counter += 1
print(queue[counter])