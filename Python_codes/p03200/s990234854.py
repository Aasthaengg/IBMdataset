s = input()
s = list(s)


w_sum = 0
w_n = 0
for i, c in enumerate(s):
    if c == "W":
        w_sum += i
        w_n += 1
    
print(w_sum - w_n*(w_n-1)//2)