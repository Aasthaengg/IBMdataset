rewards = 0

c, d = input().split(" ")

rewards += 300000 if c == "1" else 0
rewards += 200000 if c == "2" else 0
rewards += 100000 if c == "3" else 0

rewards += 300000 if d == "1" else 0
rewards += 200000 if d == "2" else 0
rewards += 100000 if d == "3" else 0

rewards += 400000 if c == "1" and d == "1" else 0
  
print(rewards)