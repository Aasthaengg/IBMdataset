no=input()
l=len(no)
flag=0
for i in range(l-1):
    if no[i]==no[i+1]:
        print("Bad")
        exit()
print("Good")