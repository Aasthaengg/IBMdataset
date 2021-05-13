s=input()
for i in range(int(len(s)/2)):
    tmp=s[:-int((i+1)*2)]
    a=0
    for j in range(int(len(tmp)/2)):
        if tmp[j]==tmp[j+int(len(tmp)/2)]:
            a+=1
    if a==int(len(tmp)/2):
        print(len(tmp))
        exit()