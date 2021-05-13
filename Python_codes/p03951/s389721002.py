N = int(input())
s = input()
t = input()
count = 0
num_s = len(s)
num_t = len(t)

for i in range(num_t):
    for j in range(i, num_s):
        if t[count] == s[j]:
            count += 1
        else:
            count = 0
            break

    if count == num_t - i:
        break
print(num_s+num_t-count)
    
