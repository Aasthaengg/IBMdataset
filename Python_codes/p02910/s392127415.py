s = input()
odd = ["R","U","D"]
even = ["L","U","D"]
res = "Yes"
for i in range(len(s)):
    if i%2 == 0 and s[i] not in odd: res = "No"
    elif i%2==1 and s[i] not in even:res="No"
print(res)