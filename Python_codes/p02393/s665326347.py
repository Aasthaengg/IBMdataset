import sys

#input_line1 = raw_input()
#input_line2 = raw_input()
#input_line3 = raw_input()



data = sys.stdin.readline()
data = data.rstrip()

#data[1] = sys.stdin.readline()
#data[2] = sys.stdin.readline()
data = data.split()

#data[0] = data[0].rstrip()
#data[1] = data[1].rstrip()
#data[2] = data[2].rstrip()


for i in range(3):
    j = i + 1
    for j in range(j,3):

        #print(j)
        if data[i] > data[j]:
           
           temp = data[i]
           data[i] = data[j]
           data[j] = temp


print"%s %s %s" % (data[0], data[1], data[2])

    

#print(input_line1)
#print(input_line2)
#print(input_line3)