a,b = input().split()
dic = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
if dic[a] > dic[b]:
    print(">")
elif dic[a] == dic[b]:
    print("=")
else:
    print("<")