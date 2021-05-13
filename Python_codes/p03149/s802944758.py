check = list(input().split())
check.sort(key=int)
if check[0] == "1" and check[1] == "4" and check[2] == "7" and check[3] == "9":
    print("YES")
else:
    print("NO")