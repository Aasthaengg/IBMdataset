def calcMax(i):
  now = numbers[i]

  future_max = max(numbers[i+1:])
  #print(numbers[i+1:])
  t = numbers[i+1:]
  #print((max(t)))
  return future_max - now

n = int(input())

numbers = []
for i in range(n):
  numbers.append(int(input()))

m = -1000000001
ti = 1000000001
for i in range(len(numbers) - 1):
    if numbers[i] < ti:
      if (i == 0 or i == len(numbers) - 1 or (numbers[i-1] >= numbers[i] and numbers[i] <= numbers[i+1])):
        temp = calcMax(i)
        #print("temp: " + str(temp))
        if temp > m:
            m = temp
            ti = numbers[i]

print (m)
