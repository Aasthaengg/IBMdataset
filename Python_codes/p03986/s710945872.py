X = input()
 
val = len(X)
sum = 0
for i in X:
    if i == "S":
        sum += 1
    else:
        if sum > 0:
            val -= 2
            sum -= 1
 
print(val)