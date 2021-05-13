a, b = list(input().split())

if a == "A":
    a = "10"
if a == "B":
    a = "11"
if a == "C":
    a = "12"
if a == "D":
    a = "13"
if a == "E":
    a = "14"
if a == "F":
    a = "15"

if b == "A":
    b = "10"
if b == "B":
    b = "11"
if b == "C":
    b = "12"
if b == "D":
    b = "13"
if b == "E":
    b = "14"
if b == "F":
    b = "15"

a=int(a)
b=int(b)

if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("=")