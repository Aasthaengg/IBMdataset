#A
b = input()
t = {"A":"T","T":"A", "C":"G","G":"C"}

result = ""

for i in b:
    result += t[i]
    
print(result)