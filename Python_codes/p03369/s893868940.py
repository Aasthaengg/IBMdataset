to = list(input())
counter = 0

if to[0] == "o":
  counter += 1
if to[1] == "o":
  counter += 1
if to[2] == "o":
  counter += 1
    
price = 700 + 100 * int(counter)

print(price)