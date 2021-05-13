s = input()
k = int(input())
if s[0] != "1":
    print(s[0])
elif s[:k].replace("1","")=="":
    print("1")
else:
    print(s.replace("1","")[0])