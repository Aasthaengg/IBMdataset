s = list(input())
t = list(input())


flag = True

for i in range(len(s)):
    s.insert(0,s.pop(-1))
    if "".join(s) == "".join(t):
        print("Yes")
        flag = False
        break



if flag:
    print("No")