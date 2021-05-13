# input
n = list(input())

op = ""
for i in n:
    if i == "1":
        op += "9"
    else:
        op += "1"

print(op)