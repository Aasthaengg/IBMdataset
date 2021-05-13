line = map(int,input().split())
line_list= list(line)
if line_list.count(line_list[0]) == 3:
    print("Yes")
else:
    print("No")
