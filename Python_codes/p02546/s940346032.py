line = input()
 
if line[len(line)-1] == ("s"):
  line += "es"
else:
  line += "s"
print(line)