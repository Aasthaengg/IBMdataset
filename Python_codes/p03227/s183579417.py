A = input()
chars = list(A)

result ="0"
if len(A)==2:
    result = A
else:
    result= chars[2]+chars[1]+chars[0]

print(result)
