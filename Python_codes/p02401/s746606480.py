while True:
    v = input().split()
   
    if v[1] == "?": break
    if v[1] == "+":
        print(int(v[0]) + int(v[2]))
    if v[1] == "-":
        print(int(v[0]) - int(v[2]))
    if v[1] == "*":
        print(int(v[0]) * int(v[2]))
    if v[1] == "/":
        print(int(v[0]) // int(v[2]))