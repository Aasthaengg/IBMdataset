t = input()
l = t.split(" ")
N = int(l[0])
K = int(l[1])
count = 0
numbers = list(range(1, N+1))
while True:
    if len(numbers) >= K:
        numbers.pop(0)
        count = count + 1
    else:
        print(count)
        break
