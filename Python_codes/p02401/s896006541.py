
n = 0
while n != 1:
 m = raw_input().split()
 if m[1] == "?":
     break

 if m[1] == "+":
     print int(m[0])+int(m[2])
 if m[1] == "-":
     print int(m[0])-int(m[2])
 if m[1] == "*":
     print int(m[0])*int(m[2])
 if m[1] == "/":
     print int(m[0])/int(m[2])