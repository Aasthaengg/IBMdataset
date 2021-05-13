X=list(input())

counter_s = 0

counter_t = 0

for i in range(len(X)):
    if counter_s == 0 and X[i] == 'T':
        counter_t += 1
    elif 0 < counter_s and X[i] == 'T':
        counter_s -= 1
    elif X[i] == 'S':
        counter_s += 1
print(counter_s+counter_t)
