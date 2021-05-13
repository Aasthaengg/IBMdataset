length=int(input())
s=input()
string = ""
if len(s) <= length:
    print(s)

else:
    for i in range(0,length):
        string += s[i]
    string +="..."

    print(string)