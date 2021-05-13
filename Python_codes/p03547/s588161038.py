input1 = list(input().split())
check = sorted(input1)
if check[0] == check[1]:
    print("=")
elif check[0] == input1[0]:
    print("<")
else:
    print(">")