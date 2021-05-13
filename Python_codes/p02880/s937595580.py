n = int(input())
s = 0
if n > 81:
    print("No")
    exit()
for i in range(1 , 10):
    if n % i == 0 and n // i < 10:
        s = "Yes"
    else:
        s = "No"
    if s == "Yes":
        print(s)
        exit()
print(s)