s = input()
odd = ["R","U","D"]
even = ["L","U","D"]
cnt = 0
for i in s[::2]:
    if i in odd:
        cnt += 1
for j in s[1::2]:
    if j in even:
        cnt += 1
        
print("Yes") if cnt == len(s) else print("No")