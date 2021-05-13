word=input().rstrip()
flag=0
if word[2]==word[3]:
    if word[4]==word[5]:
        flag=1
if flag:
    print("Yes")
else:
    print("No")