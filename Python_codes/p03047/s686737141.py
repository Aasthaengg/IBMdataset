from sys import stdin
input=input=stdin.readline().rstrip().split()
for i in range(len(input)):
  input[i]=int(input[i])
#print(input)

output=input[0]-(input[1]-1)
print(output)