import sys
input()
dic = {}
line = map(lambda x:x.split(), sys.stdin.readlines())
for i in line:
    if i[0] == "insert":
        dic[i[1]] = None
    else:
        print("yes" if i[1] in dic else "no")