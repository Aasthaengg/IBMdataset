akiba = ["KIH", "B", "R", ""]
s=input()
for bit in range(2**4):
    a=""
    for i in range(4):
        if bit>>i & 1:
            a+="A"
        a+=akiba[i]
    if s==a:
        print("YES")
        exit()
    
print("NO")