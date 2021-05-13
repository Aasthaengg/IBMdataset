a = [int(input()) for _ in range(5)]

loss = [(10-i%10)%10 for i in a]

print(sum(a+loss)-max(loss))