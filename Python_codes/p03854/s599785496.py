s = input()
 
kouho = ["dream", "dreamer", "erase", "eraser"]
 
s = s.replace(kouho[3], "").replace(kouho[2], "").replace(kouho[1], "").replace(kouho[0], "")
 
if s == "":
    print("YES")
else:
    print("NO")