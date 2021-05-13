import sys

string = raw_input()
string_list = list(string)
#print string_list
q = input()

for i in range(q):
    x = map(str, raw_input().split())
    if(x[0] == 'replace'):
        k = 0
        for j in range(int(x[1]), int(x[2])+1):
            string_list[j] = x[3][k]
            k += 1
        #print "".join(string_list)
    if(x[0] == 'reverse'):
        temp = []
        for j in range(int(x[1]), int(x[2])+1):
            temp.append(str(string_list[j]))
        temp.reverse()
        #print temp        
        temp_list = list(temp)
        k = 0
        for j in range(int(x[1]), int(x[2])+1):
           string_list[j] = temp[k]
           k += 1
        #print "".join(string_list)
    if(x[0] == 'print'):
        for i in range(int(x[1]), int(x[2])+1):
          sys.stdout.write(string_list[i])
        print