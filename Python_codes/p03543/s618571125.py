s = str(input())
li = list(map(int, s))
if (li[0]==li[1]&li[1]==li[2])or(li[1] == li[2]&li[2]==li[3]):
    print("Yes")
else:
    print("No")