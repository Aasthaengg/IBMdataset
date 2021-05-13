def find():
    a=input()
    c=a.split('hi')
    for i in c:
        if i!="":
            return "No"
    return "Yes"
print(find())