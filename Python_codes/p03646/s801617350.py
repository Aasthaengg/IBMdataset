data = int(input())

counter = 50
q = data // counter
r = data % counter

a = (counter - 1 + q) + counter - (r - 1)
b = (counter - 1 + q) - r

answer = [a] * r + [b] * (counter - r)
print(counter)
print(' '.join(list(map(str, answer))))