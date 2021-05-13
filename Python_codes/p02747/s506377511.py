S = input()
n = len(S)
result = "Yes"
if n%2 :
    result = "No"
else:
    for i in range(n):
        if i % 2 == 0 and S[i] == "h":
            i = i +1
        elif i % 2 and S[i] == "i":
            i = i + 1
        else:
            result = "No"
            break
print(result)
