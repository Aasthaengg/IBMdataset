n = int(input())
s = input()
x = 0
point = [0] * (n + 1)
for i in range(n) :
    if s[i] == "I" :
        point[i+1] = point[i] + 1
    if s[i] == "D" :
        point[i+1] = point[i] - 1
print(max(point))
