n = int(input())
dict = {}
command = [(input().split()) for i in range(n)]
for c in command:
    if(c[0] == "insert"):
        dict[c[1]] = 1
    elif(c[0] == "find"):
        if(c[1] in dict):
            print('yes')
        else:
            print('no')

