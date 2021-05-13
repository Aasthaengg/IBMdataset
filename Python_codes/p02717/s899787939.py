abc = input()
indiv = abc.split(" ")

#Swap A and B
temp = indiv[0]
indiv[0] = indiv[1]
indiv[1] = temp

#Swap A and C
temp = indiv[2]
indiv[2] = indiv[0]
indiv[0] = temp

print(indiv[0] + " " + indiv[1] + " " + indiv[2])
