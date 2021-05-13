n = int(input())
dic = set()
for i in range(n):
    Cmd, Key = input().split(" ")
    if Cmd == "insert":
	    dic.add(Key)
    else:
        if Key in dic:
	        print("yes")
        else:
            print("no")