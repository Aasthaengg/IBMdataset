s = input()
rs = s[::-1]
a = s.find('A')
z = rs.find('Z')
z = len(s)-z
count = z - a 
print(count)